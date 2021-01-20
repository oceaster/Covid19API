# LOCAL APP IMPORTS
from api.travel import fetch

UK_name = 'United Kingdom'
UK_data = None
US_name = 'United States'
US_data = None


def test_case_data():
    UK_data = fetch.case_data(UK_name)
    assert UK_data is not None
    assert 'message' not in UK_data
    US_data = fetch.case_data(US_name)
    assert US_data is not None
    assert 'message' not in US_data
    assert UK_data[0]['Country'] == "United Kingdom"
    assert US_data[0]['Country'] == "United States of America"


def test_data_request():
    data = fetch._loc_dest_data_(UK_name, US_name)
    assert isinstance(data, dict)
    assert len(data) == 2
    assert UK_name in data
    assert US_name in data
    assert isinstance(data[UK_name], list)
    assert isinstance(data[US_name], list)
    assert data[UK_name][0]['Country'] == "United Kingdom"
    assert data[US_name][0]['Country'] == "United States of America"


def test_data():
    state = fetch.compare(UK_name, US_name)
    assert state[UK_name] >= 0
    assert state[US_name] >= 0
    assert state[UK_name] < state[US_name] or state[UK_name] > state[US_name]
