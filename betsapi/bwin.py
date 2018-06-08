#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import json
from .baseapi import BaseBetsAPI


v1_bet365='https://api.betsapi.com/v1/bet365'

class BWin(BaseBetsAPI):
    r"""BWin library.  
    """    
    
    def __init__(self, token):
        self.token = token

        # English by default
        self.LNG_ID = '1' 

        self._inplay = 'https://api.betsapi.com/v1/bwin/inplay'
        self._event = 'https://api.betsapi.com/v1/bwin/event'
        self._prematch = 'https://api.betsapi.com/v1/bwin/prematch'
        self._result = 'https://api.betsapi.com/v1/bwin/result'
        
       
    def inplay(self): 
        r"""BWin InPlay  
        """
        params = {
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._inplay, params=params)
        return json.loads(req.content)

    def event(self, event_id):
        r"""BWin Event  
        
        :param `event_id`:(required),Event ID you get from /bwin/inplay or prematch.  
        you can send multiple `event_ids` in one request with `event_id`=1,2,3,4 up to max 10 ids.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event, params=params)
        return json.loads(req.content)
       
    def prematch(self,day=None,sport_id=None,league_id=None):
        r"""BWin Prematch Odds  

        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `sport_id`:(optional),BWin sport_id.  
        :param `league_id`:(optional),BWin league_id.  
        """
        params = {
            'token': self.token
        }
        
        if day:
            params['day'] = day
        if sport_id:
            params['sport_id'] = sport_id
        if league_id:
            params['league_id'] = league_id
        

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._prematch, params=params)
        return json.loads(req.content)
       
    def result(self, event_id):
        r"""BWin Result  
        Note a few of (less than 3%) events are not covered.  

        :param `event_id`:required,eventid from BWin API.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._result, params=params)
        return json.loads(req.content)

        