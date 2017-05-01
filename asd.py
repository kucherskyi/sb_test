import requests
import json

API_KEY = 'a75f8969f7e39790bacd7b410adf2c817567155cbc201063b3b3acc82698325d'
AUTH_URL = 'http://user-api.simplybook.me'
ADMIN_URL = 'http://user-api.simplybook.me/admin'
COMPANY_LOGIN = 'artemtest'
USER = 'admin'
USER_PWD = 'nezybevud'


'''setWorkDayInfo ($info)
Set work day schedule
for company | service | provider
for week_day | date

Example:

    {
        "start_time": "10:00",
        "end_time": "18:00",
        "is_day_off": 0,
        "breaktime": [{
            "start_time": "14:00",
            "end_time": "15:00"
        }],
        "index": "1",
        "name": "Monday",
        "date": "",
        "unit_group_id": "1",
        "event_id": "1"
    }
'''


def setUp():
    admin_params = {
        "method": "getUserToken",
        "params": [COMPANY_LOGIN, USER, USER_PWD],
        "id": 0
    }
    admin_token = requests.post(AUTH_URL + '/login',
                                data=json.dumps(admin_params)).json()['result']

    def set_days():
        set_day = {
            "start_time": "10:00",
            "end_time": "18:00",
            "is_day_off": 0,
            "breaktime": [{
                "start_time": "14:00",
                "end_time": "15:00"
            }],
            "index": "1",
            "name": "",
            "date": "2017-05-03",
            "unit_group_id": 2,
            "event_id": 2
        }
        set_params = {
            "method": "setWorkDayInfo",
            "params": set_day,
            "jsonrpc": "2.0",
            "id": 1
        }
        admin_headers = {'X-Company-Login': COMPANY_LOGIN,
                         'X-User-Token': admin_token,
                         'content-type': 'application/json'}

        set_days_request = requests.post(ADMIN_URL, headers=admin_headers,
                                         data=json.dumps(set_params))
        import pdb
        pdb.set_trace()
        print 'asd'
        return set_days_request

    getToken_params = {
        "method": "getToken",
        "params": [COMPANY_LOGIN, API_KEY],
        "id": 0}

    token = requests.post(AUTH_URL + '/login',
                          data=json.dumps(getToken_params)).json()['result']

    headers = {
        'X-Company-Login': COMPANY_LOGIN,
        'X-Token': token,
        'content-type': 'application/json'
    }

    get_params = {
        "method": "getStartTimeMatrix",
        "params": ['2017-05-01 09:00:00', '2017-05-11 10:00:00', 2, 2],
        "jsonrpc": "2.0",
        "id": 1
    }

    def ret(parms):
        units_list = requests.post(AUTH_URL, headers=headers,
                                   data=json.dumps(parms))
        return units_list
    import pdb
    pdb.set_trace()
    print 'asd'

setUp()