# -*- coding:utf-8 -*-

import os
import sys
import json
import requests


class BaseBetsAPI(object):


    def __init__(self):

        self.token = None


    def build_uri(self, url, endpoint):
        r"""
        :param `url`:(required), url should not end with '/'.  
        :param `endpoint`:(required),endpoint should not start with '/'.  
        """
        return '/'.join([url, endpoint])

    def set_lng(self, lng_id):
        r"""set language.  
        :param `lng_id`:(required),see [faq](https://betsapi.com/docs/events/faq.html) for more details.  
        """
        self.LNG_ID = str(lng_id)
