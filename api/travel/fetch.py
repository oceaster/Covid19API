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
    Compares the data of location & destination data sets.
    While making sure that data gathered for a country is
    from the latest available date - not considering time.
    When no data can match the requirements 0 is returned.

    Parameters:
        data (dict/json): containing 'location' & 'destination' keys

    Returns:
        boolean:
            true when location data has less confirmed cases than destination
            false when location data has more confirmed cases than destination
    '''
    data = _loc_dest_data_(location, destination)

    # MOST RECENT DATE FOR DATA ON LOC/DES
    if len(data[location]) > 0:
        loc_date = data[location][-1]['Date'].split('T')[0]
    else:
        loc_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

    if len(data[destination]) > 0:
        des_date = data[destination][-1]['Date'].split('T')[0]
    else:
        des_date = loc_date

    # CREATE DEFAULT CASE DATA
    case = {
        location: 0,
        destination: 0
    }

    # ITERATE DATES FOR MOST RECENT DATE
    for dat in data[location]:
        if dat["Date"].split('T')[0] == loc_date:
            case[location] += dat["Active"]

    for dat in data[destination]:
        if dat["Date"].split('T')[0] == des_date:
            case[destination] += dat["Active"]

    return case


def permit(loc, des, age, trv, rtn=None):
    age = int(age)
    trv = datetime.strptime(trv, '%Y-%m-%d')
    rtn = datetime.strptime(rtn, '%Y-%m-%d')
    resp = {}
    warn = []
    min_travel_date = datetime.now() - timedelta(-2)
    max_travel_date = datetime.now() - timedelta(-5)
    min_return_date = datetime.now() - timedelta(-2)
    max_return_date = datetime.now() - timedelta(-60)

    # TRAVEL DATE CONDITION CHECK
    if min_travel_date <= trv <= max_travel_date:
        resp['travel_date'] = True
    else:
        warn.append('date of travel must be within 2-5 working days')
        resp['travel_date'] = False

    # RETURN DATE CONDITION CHECK
    if min_return_date <= rtn <= max_return_date or rtn is None:
        resp['return_date'] = True
    else:
        warn.append('date of return must be within 2 months')
        resp['return_date'] = False

    # AGE CONDITION CHECK
    if age < 21:
        if age >= 15:
            resp['age'] = True
            warn.append('must travel with adult')
        else:
            resp['age'] = False
            warn.append('too young to travel')
    else:
        resp['age'] = True

    # LOC/DES CONDITION CHECK
    case_data = compare(loc, des)

    if case_data[loc] == 0:
        warn.append('no case data available for your current location')
    if case_data[des] == 0:
        warn.append('no case data available for your selected destination')

    if case_data[loc] <= case_data[des]:
        resp['loc_to_des'] = True
    else:
        warn.append('location case data is higher than destination case data')
        resp['loc_to_des'] = False

    # JSON RESPONSE
    resp['warnings'] = warn
    return resp
