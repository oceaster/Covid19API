# MODULE IMPORTS
from django.http.response import JsonResponse

# LOCAL API IMPORTS
from api.travel.fetch import compare


def fetch_comparison(req, location, destination, *args, **kwargs):
    return JsonResponse(
        compare(
            location=location,
            destination=destination
        )
    )

