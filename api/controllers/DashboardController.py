from api.services.DashboardService import DashboardService

def index():
    return DashboardService.dashboardData()