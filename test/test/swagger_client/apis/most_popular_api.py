# coding: utf-8

"""
    Most Popular

    Provides services for getting the most popular articles on NYTimes.com based on emails, shares, or views.  Get most emailed articles for the last day: ``` /emailed/1.json ```  Get most shared articles on Facebook for the last day: ``` /shared/1/facebook.json ```  Get most viewed articles for the last seven days: ``` /viewed/7.json ```  ## Example Calls ``` https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/mostpopular/v2/shared/1/facebook.json?api-key=yourkey ```  ``` https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=yourkey ``` 

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MostPopularApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def emailed_period_json_get(self, period, **kwargs):
        """
        Most emailed articles on NYTimes.com.
        Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.emailed_period_json_get(period, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.emailed_period_json_get_with_http_info(period, **kwargs)
        else:
            (data) = self.emailed_period_json_get_with_http_info(period, **kwargs)
            return data

    def emailed_period_json_get_with_http_info(self, period, **kwargs):
        """
        Most emailed articles on NYTimes.com.
        Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.emailed_period_json_get_with_http_info(period, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emailed_period_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'period' is set
        if ('period' not in params) or (params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `emailed_period_json_get`")

        resource_path = '/emailed/{period}.json'.replace('{format}', 'json')
        path_params = {}
        if 'period' in params:
            path_params['period'] = params['period']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse200',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def shared_period_json_get(self, period, **kwargs):
        """
        Most shared articles on NYTimes.com.
        Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shared_period_json_get(period, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.shared_period_json_get_with_http_info(period, **kwargs)
        else:
            (data) = self.shared_period_json_get_with_http_info(period, **kwargs)
            return data

    def shared_period_json_get_with_http_info(self, period, **kwargs):
        """
        Most shared articles on NYTimes.com.
        Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shared_period_json_get_with_http_info(period, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shared_period_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'period' is set
        if ('period' not in params) or (params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `shared_period_json_get`")

        resource_path = '/shared/{period}.json'.replace('{format}', 'json')
        path_params = {}
        if 'period' in params:
            path_params['period'] = params['period']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2001',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def shared_period_share_type_json_get(self, period, share_type, **kwargs):
        """
        Most shared articles on NYTimes.com of specified share type.
        Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shared_period_share_type_json_get(period, share_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :param str share_type: Share type: facebook. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.shared_period_share_type_json_get_with_http_info(period, share_type, **kwargs)
        else:
            (data) = self.shared_period_share_type_json_get_with_http_info(period, share_type, **kwargs)
            return data

    def shared_period_share_type_json_get_with_http_info(self, period, share_type, **kwargs):
        """
        Most shared articles on NYTimes.com of specified share type.
        Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.shared_period_share_type_json_get_with_http_info(period, share_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :param str share_type: Share type: facebook. (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period', 'share_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shared_period_share_type_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'period' is set
        if ('period' not in params) or (params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `shared_period_share_type_json_get`")
        # verify the required parameter 'share_type' is set
        if ('share_type' not in params) or (params['share_type'] is None):
            raise ValueError("Missing the required parameter `share_type` when calling `shared_period_share_type_json_get`")

        resource_path = '/shared/{period}/{share_type}.json'.replace('{format}', 'json')
        path_params = {}
        if 'period' in params:
            path_params['period'] = params['period']
        if 'share_type' in params:
            path_params['share_type'] = params['share_type']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2001',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def viewed_period_json_get(self, period, **kwargs):
        """
        Most viewed articles on NYTimes.com.
        Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.viewed_period_json_get(period, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.viewed_period_json_get_with_http_info(period, **kwargs)
        else:
            (data) = self.viewed_period_json_get_with_http_info(period, **kwargs)
            return data

    def viewed_period_json_get_with_http_info(self, period, **kwargs):
        """
        Most viewed articles on NYTimes.com.
        Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days). 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.viewed_period_json_get_with_http_info(period, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int period: Time period: 1, 7, or 30 days. (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['period']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method viewed_period_json_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'period' is set
        if ('period' not in params) or (params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `viewed_period_json_get`")

        resource_path = '/viewed/{period}.json'.replace('{format}', 'json')
        path_params = {}
        if 'period' in params:
            path_params['period'] = params['period']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['apikey']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2002',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))