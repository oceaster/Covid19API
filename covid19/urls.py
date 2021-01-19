# DJANGO MODULES
from django.urls import path

# LOCAL IMPORTS
from client.views import index, robots
from api.views import fetch_comparison, fetch_permit

# APP URLS
urlpatterns = [
    # CORE PATHS
    path('', index),
    path('robots.txt', robots),
    # TRAVEL API PATHS
    path(
        'api/compare/<location>/<destination>',
        fetch_comparison
    ),
    path(   # Permit with return date
        'api/permit/<location>/<destination>/<age>/<travel_date>/<return_date>',
        fetch_permit
    ),
    path(   # Permit with no return date
        'api/permit/<location>/<destination>/<age>/<travel_date>',
        fetch_permit
    )
]
