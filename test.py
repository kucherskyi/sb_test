import json
import requests
from base_test import BaseTestCase


class TestGetStartTimeMatrix(BaseTestCase):

    def test_function(self):
        params = self.func_params('2017-05-01')
        units_list = requests.post(self.AUTH_URL, headers=self.headers,
                                   data=json.dumps(params))
