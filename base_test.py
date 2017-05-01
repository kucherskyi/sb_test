import requests
from unittest import TestCase
import json

API_KEY = 'a75f8969f7e39790bacd7b410adf2c817567155cbc201063b3b3acc82698325d'
COMPANY_LOGIN = 'artemtest'


class BaseTestCase(TestCase):
    """ Here is a basic test case class with getting token.
    It's not needed for my particular task, but in case of future extention,
    i think, better to have setup separately.
    """
    AUTH_URL = 'http://user-api.simplybook.me'

    def setUp(self):
        token_params = {"method": "getToken",
                        "params": [COMPANY_LOGIN, API_KEY],
                        "id": 0}
        token = requests.post(self.AUTH_URL + '/login',
                              data=json.dumps(token_params)).json()['result']
        self.headers = {'content-type': 'application/json',
                        'X-Company-Login': COMPANY_LOGIN,
                        'X-Token': token}

    def func_params(self, *args, **kwargs):
        request_params = {"method": "getStartTimeMatrix",
                          "params": [args, kwargs],
                          "jsonrpc": "2.0",
                          "id": 1}
        return request_params
