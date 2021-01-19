# MODULE IMPORTS
from json.encoder import JSONEncoder
from django.http.response import JsonResponse

# LOCAL API IMPORTS
from api.travel.fetch import compare, permit


def fetch_comparison(req, location, destination, *args, **kwargs):
    return JsonResponse(
        compare(
            location=location,
            destination=destination
        )
    )


def fetch_permit(
    req, location, destination, age,
    travel_date, return_date=None, *args, **kwargs
    ):
    return JsonResponse(
        permit(
            loc=location,
            des=destination,
            age=age,
            trv=travel_date,
            rtn=return_date
        )
    )
