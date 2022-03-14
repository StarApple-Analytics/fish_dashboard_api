import logging.config
from os import environ
from dotenv import load_dotenv
from pandas import read_csv, read_sql
from flask_cors import CORS
from flask import Flask, redirect
from .config import config as app_config
from .swaggerConfig import config as swaggerConfig
from .extentions import db, ma
from .constant import FISH_CSV_DIR
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():

    # loading env vars from .env file
    load_dotenv()
    APPLICATION_ENV = get_environment()
    logging.config.dictConfig(app_config[APPLICATION_ENV].LOGGING)
    app = Flask(app_config[APPLICATION_ENV].APP_NAME)
    app.config.from_object(app_config[APPLICATION_ENV])

    # Plugins initialization goes here
    db.init_app(app)
    ma.init_app(app)

    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        swaggerConfig.SWAGGER_URL,
        swaggerConfig.API_URL,
        config={"app_name": "Fishes API"},
    )
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # --------------------------------
    # Module Imports
    # --------------------------------

    # Import Models
    from api.models import Fish

    # Imports Schemas
    from api.schemas import FishSchema

    # Import the module / component using their blueprints
    from api.routes import API_ROUTES

    # Register Blueprints

    for api_blueprint in API_ROUTES:
        app.register_blueprint(api_blueprint, url_prefix="/api/")

    # Register Swagger Blueprint
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix="/docs/")

    @app.before_first_request
    def populate_tables():
        db.create_all()
        # Check if the existing table contain data, if not then initialize with csv insert
        s = db.session()
        if len(s.query(Fish.Fish).all()) == 0:
            print("No data in the table detected.")
            print("Initialising the table in database.")
            engine = s.get_bind()
            df = read_csv(FISH_CSV_DIR)
            df = df.rename(columns=str.lower)
            df = df.rename(columns={"length1": "vertical_length", "length2": "horizontal_length", "length3": "diagonal_length"})
            df.to_sql(
                "fishes", con=engine, if_exists="append", chunksize=1000, index=False
            )

    @app.route("/")
    def toDocs():
        return redirect("/docs/")

    return app


def get_environment():
    return environ.get("APPLICATION_ENV") or "development"
