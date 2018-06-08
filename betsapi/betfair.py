#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import json
from .baseapi import BaseBetsAPI


class Betfair(BaseBetsAPI):
    r"""Betfair library.  

    Sportsbook and Exchange:  
    `Sportsbook` API is related to Sportsbook tab as https://www.betfair.com/sport/.  
    `Exchange` API is related to Exchange tab as https://www.betfair.com/exchange/plus/.  
    """
    
    def __init__(self, token):
        
        self.token = token
        # English by default
        self.LNG_ID = '1' 

        self._sb_inplay = 'https://api.betsapi.com/v1/betfair/sb/inplay'
        self._sb_upcoming = 'https://api.betsapi.com/v1/betfair/sb/upcoming'
        self._sb_event = 'https://api.betsapi.com/v1/betfair/sb/event'
        self._ex_inplay = 'https://api.betsapi.com/v1/betfair/ex/inplay'
        self._ex_upcoming = 'https://api.betsapi.com/v1/betfair/ex/upcoming'
        self._ex_event = 'https://api.betsapi.com/v1/betfair/ex/event'
        self._timeline = 'https://api.betsapi.com/v1/betfair/timeline'
        self._result = 'https://api.betsapi.com/v1/betfair/result'
    
    def sb_inplay(self, sport_id=None,page=None):
        r"""Sportsbook InPlay    
        
        :param `sport_id`:(optional),Betfair eventTypeId.  
        :param `page`:(optional),see [R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager)for more details.          
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

        req = requests.get(self._sb_inplay, params=params)
        return json.loads(req.content)

    def sb_upcoming(self, sport_id=None,day=None,page=None):
        r"""Sportsbook Upcoming   

        :param `sport_id`:(optional),Betfair eventTypeId.  
        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `page`:(optional),see [R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager) for more details.  
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

        req = requests.get(self._sb_inplay, params=params)
        return json.loads(req.content)

    def sb_event(self, event_id):
        r"""Sportsbook Event  

        :param `event_id`:(required),Event ID you get from /betfair/inplay or upcoming.  
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._sb_inplay, params=params)
        return json.loads(req.content)

    def ex_inplay(self, sport_id=None,page=None):
        r"""Exchange InPlay  

        :param `sport_id`:(optional),Betfair eventTypeId.  
        :param `page`:(optional),see [R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager)for more details.          
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

        req = requests.get(self._sb_inplay, params=params)
        return json.loads(req.content)

    def ex_upcoming(self, sport_id=None,day=None,page=None):
        r"""Exchange Upcoming  

        :param `sport_id`:(optional),Betfair eventTypeId.  
        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `page`:(optional),see [R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager) for more details.  
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

        req = requests.get(self._sb_inplay, params=params)
        return json.loads(req.content)

    def ex_event(self, event_id):
        r"""Exchange Event  

        :param `event_id`:(required),Event ID you get from /betfair/inplay or upcoming.  
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._sb_inplay, params=params)
        return json.loads(req.content)

    def timeline(self,event_id):
        r"""Betfair Timeline

        :param `event_id`:(required),Event ID you get from /betfair/inplay.  
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._timeline, params=params)
        return json.loads(req.content)

    def result(self,event_id):
        r"""Betfair Result  
        Note a few of (less than 3%) events are not covered.  

        :param `event_id`:(required),Event ID you get from /betfair/inplay.  
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._result, params=params)
        return json.loads(req.content)
        