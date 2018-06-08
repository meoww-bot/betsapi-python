#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import json
from .baseapi import BaseBetsAPI


class Sbobet(BaseBetsAPI):
    r"""Sbobet library.  
    """

    def __init__(self, token):
        self.token = token

        # English by default
        self.LNG_ID = '1' 

        self._inplay = 'https://api.betsapi.com/v1/sbobet/inplay'
        self._upcoming = 'https://api.betsapi.com/v1/sbobet/upcoming'
        self._event = 'https://api.betsapi.com/v1/sbobet/event'
        self._result = 'https://api.betsapi.com/v1/sbobet/result'

    def inplay(self, sport_id=None,page=None):
        r"""Sbobet InPlay  

        :param `sport_id`:(optional),[R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid) (only 1-Soccer is supported now).  
        :param `page`:(optional),[R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager).
        """
        params = {
            'token': self.token
        }

        if sport_id:
            params['sport_id'] = sport_id
        
        if page:
            params['page'] = page

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._inplay, params=params)
        return json.loads(req.content)

    def upcoming(self, sport_id=None,day=None,page=None):
        r"""Sbobet Upcoming  

        :param `sport_id`:(optional),[R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid) (only 1-Soccer is supported now).  
        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `page`:(optional),[R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager).
        """
        params = {
            'token': self.token
        }

        if sport_id:
            params['sport_id'] = sport_id
        if day:
            params['day'] = day
        if page:
            params['page'] = page

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._upcoming, params=params)
        return json.loads(req.content)

    def event(self, event_id):
        r"""Sbobet Event  

        :param `event_id`:(required),Event ID you get from /sbobet/inplay or upcoming.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event,params=params)
        return json.loads(req.content)

    def result(self, event_id):
        r"""Sbobet Result  
        Note a few of (less than 2%) events are not covered.

        :param `event_id`:(required),Event Id from Sbobet API.  
        you can send multiple event_ids in one request with event_id=1,2,3,4 up to max 10 ids.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._result, params=params)
        return json.loads(req.content)