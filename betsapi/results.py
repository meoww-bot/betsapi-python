#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import json
from .baseapi import BaseBetsAPI

class Results(BaseBetsAPI):
    r"""Results library.  
    """
    
    def __init__(self, token):
        self.token = token
        
        # English by default
        self.LNG_ID = '1' 

        self._betfred= 'https://api.betsapi.com/v1/betfred/result'
        self._williamhill= 'https://api.betsapi.com/v1/williamhill/result'
        self._sbobet= 'https://api.betsapi.com/v1/sbobet/result'
        self._betsson= 'https://api.betsapi.com/v1/betsson/result'
    
    def betfred(self,event_id):
        r"""BetFred Result  
        Note a few of (less than 2%) events are not covered.  
        Useful that you want the results by querying with BetFred XML Feed.  
        
        :param `event_id`:(required),event_id from BetFred XML Feeds. (.20 will be removed automatically).  
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._betfred, params=params)
        return json.loads(req.content)

    def williamhill(self,event_id ):
        r"""WilliamHill Result  
        Note a few of (less than 2%) events are not covered.  
        Useful that you want the results by querying with WilliamHill XML Feed.  

        :param `event_id`:(required),event_id from WilliamHill XML Feeds. (Example: the id 10901582 is from url http://sports.williamhill.com/bet/en-gb/betting/e/10901582/)

        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._williamhill, params=params)
        return json.loads(req.content)

    def sbobet(self, event_id):
        r"""Sbobet Result  
        Note a few of (less than 2%) events are not covered.  
        Useful that you want the results by querying with Sbobet Event ID.  

        :param `event_id`:(required),event_id from Sbobet.
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._sbobet, params=params)
        return json.loads(req.content)
    
    def betsson(self,event_id ):
        r"""Betsson Result  
        Note a few of (less than 3%) events are not covered.  
        Useful that you want the results by querying with Betsson Event ID.  

        :param `event_id`:(required),event_id from Betsson.
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._betsson, params=params)
        return json.loads(req.content)