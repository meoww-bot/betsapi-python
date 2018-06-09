#!/usr/bin/env python
#-*-coding:utf-8-*-
import json
import os
import re
import sys

import requests

from .baseapi import BaseBetsAPI


class Bet365(BaseBetsAPI):
    """
    Bet365 library.  
    """    

    def __init__(self, token):
        r"""
        :param `token`: required.  
        """
        
        self.token = token

        # English by default
        self.LNG_ID = '1' 
        
        v1_bet365='https://api.betsapi.com/v1/bet365'
        
        self._inplay= self.build_uri(v1_bet365,'inplay')
        self._inplay_filter = self.build_uri(v1_bet365,'inplay_filter')
        self._inplay_event= self.build_uri(v1_bet365,'event')
        self._upcoming_events= self.build_uri(v1_bet365,'upcoming')
        self._prematch_odds= self.build_uri(v1_bet365,'start_sp')
        self._result= self.build_uri(v1_bet365,'result')
    

    def inplay(self,raw=None):
        r"""Bet365 InPlay  

        :param `raw`:(optional),raw Bet365 body without parsing. 
        """
        params = {
            'token': self.token
        }

        if raw:
            params['raw'] = raw

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._inplay, params=params)
        return json.loads(req.content)

    def inplay_filter(self,sport_id,league_id=None):
        r"""Bet365 InPlay Filter  

        :param `sport_id`:(required),see [R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid) for more details.  
        :param `league_id`:(optional),useful when you want only one league.  
        Note: there is no pager in this API call. we just return all events.  
        """
        params = {
            'sport_id':sport_id,
            'token': self.token
        }

        if league_id:
            params['league_id'] = league_id

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._inplay_filter, params=params)
        return json.loads(req.content)

    def inplay_event(self,FI,stats=None,lineup=None,raw=None):
        r"""Bet365 Inplay Event  

        :param `FI`:(required),FI from Bet365 Inplay.  
        :param `stats`: (optional),extra stats info (only provided for Soccer and Cricket).  
        :param `lineup`:(optional),lineup info (only provided for Cricket right now).
        :param `raw`:(optional),raw Bet365 body without parsing.
        """
        params = {
            'FI':FI,
            'token': self.token
        }

        if stats:
            params['stats']=stats
        if lineup:
            params['lineup']=lineup
        if raw:
            params['raw']=raw

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._inplay_event, params=params)
        return json.loads(req.content)

    def upcoming_events(self,sport_id,league_id=None,day=None,page=None):
        r"""Bet365 Upcoming Events  

        :param `sport_id`:(required),see [R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid) for more details.  
        :param `league_id`:(optional),useful when you want only one league.
        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `page`:(optional),see [R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager) for more details.
        """
        params = {
            'sport_id':sport_id,
            'token': self.token
        }
        if league_id:
            params['league_id'] = league_id
        if day:
            params['day']= day
        if page:
            params['page'] = page

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID
            

        req = requests.get(self._upcoming_events, params=params)
        return json.loads(req.content)

    def prematch_odds(self,FI,raw=None):
        r"""Bet365 PreMatch Odds  

        :param `FI`:(required),Event ID you get from bet365/upcoming.  
        :param `raw`:(optional),raw Bet365 body without parsing.  
        """
        params = {
            'FI':FI,
            'token': self.token
        }

        if raw:
            params['raw'] = raw

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._prematch_odds, params=params)
        return json.loads(req.content)

    def result(self,event_id):
        r"""Bet365 Result  
        
        :param `event_id`:(required),Event ID (FI) from Bet365 Inplay.  
        Note:you can send multiple event_ids in one request with event_id=1,2,3,4 up to max 10 ids.
        """
        params = {
            'event_id':event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._result, params=params)
        return json.loads(req.content)
