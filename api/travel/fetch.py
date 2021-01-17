from requests import request
from datetime import datetime, timedelta


def case_data(country):
    '''
    Fetches current case data on a single country from api.covid19api.com

    Parameters:
        country (string): name of a country

    Returns:
        dict (json): containing case data on specified country
    '''
    country = country.lower().replace(' ', '-')
    domain = 'https://api.covid19api.com'

    url = '{domain}/live/country/{country}/status/confirmed'.\
        format(domain=domain, country=country)
    resp = request('GET', url)

    return resp.json()


def _loc_dest_data_(location, destination):
    '''
    Fetches case data on location & destination country

    Parameters:
        location (string): name of country-of-origin
        destination (string): name of country-of-destination

    Returns:
        dict (json): containing case data on two specified countries
    '''
    location_data = case_data(location)

    if location != destination:
        destination_data = case_data(destination)
    else:
        destination_data = location_data

    return {
        location: location_data,
        destination: destination_data
    }


def compare(location, destination):
    '''
    Compares the data of location & destination data sets

    Parameters:
        data (dict/json): containing 'location' & 'destination' keys

    Returns:
        boolean:
            true when location data has less confirmed cases than destination
            false when location data has more confirmed cases than destination
    '''
    data = _loc_dest_data_(location, destination)

    if len(data[location]) > 0:
        d1 = data[location][-1]['Date'].split('T')[0]
    else:
        d1 = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
    if len(data[destination]) > 0:
        d2 = data[destination][-1]['Date'].split('T')[0]
    else:
        d2 = d1

    case = {
        location: 0,
        destination: 0
    }

    for dat in data[location]:
        if dat["Date"].split('T')[0] == d1:
            case[location] += dat["Active"]

    for dat in data[destination]:
        if dat["Date"].split('T')[0] == d2:
            case[destination] += dat["Active"]

    return case

