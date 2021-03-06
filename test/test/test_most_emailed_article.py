from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException


class TestMostEmailedArticle(unittest.TestCase):

    def setUp(self):
        apiKey = os.getenv('NYFT_API_KEY')
        self.assertNotIn(apiKey, [None, ""])
        swagger_client.configuration.api_key = {"api-key": apiKey}
        self.api = swagger_client.apis.most_popular_api.MostPopularApi()

    def tearDown(self):
        pass

    def test_can_access_only_with_valid_api_key(self):
        try:
            swagger_client.configuration.api_key = {"api-key": ""}
            response = self.api.emailed_period_json_get(period=1)
        except ApiException as e:
            self.assertEqual(e.status, 401)


    def test_period_can_be_only_1_7_30_days(self):
        periods = [1, 7, 30]
        for period in periods:
            with self.subTest():
                response = self.api.emailed_period_json_get(period=period)
                self.assertEqual(len(response.results), 20)

        periods = [-30, -7, -1, 0, 1, 8, 40]
        for period in periods:
            with self.subTest():
                try:
                    self.api.emailed_period_json_get(period=period)
                except ApiException as e:
                    self.assertEqual(e.status, 404)

    def test_response_has_20_articles(self):
        response = self.api.emailed_period_json_get(period=1)
        self.assertEqual(len(response.results), 20)


if __name__ == '__main__':
    unittest.main()
