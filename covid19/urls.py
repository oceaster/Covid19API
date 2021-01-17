# DJANGO MODULES
from django.urls import path

# LOCAL IMPORTS
from client.views import index, robots
from api.views import fetch_comparison

# APP URLS
urlpatterns = [
    # CORE PATHS
    path('', index),
    path('robots.txt', robots),
    # TRAVEL API PATHS
    path(
        'api/compare/<location>/<destination>',
        fetch_comparison
    )
]
