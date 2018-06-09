#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import json
from .baseapi import BaseBetsAPI


class Events(BaseBetsAPI):
    r"""Events library.  
    """

    def __init__(self, token):
        self.token = token

        # English by default
        self.LNG_ID = '1' 
        v1_event = 'https://api.betsapi.com/v1/event'
        v2_event = 'https://api.betsapi.com/v2/event'

        v1_events = 'https://api.betsapi.com/v1/events'
        v2_events = 'https://api.betsapi.com/v2/events'

        v1_league = 'https://api.betsapi.com/v1/league'
        v1_team = 'https://api.betsapi.com/v1/team'

        self._inplay_events = self.build_uri(v1_events, 'inplay')
        self._upcoming_events = self.build_uri(v2_events, 'upcoming')
        self._ended_events = self.build_uri(v2_events, 'ended')
        self._events_search = self.build_uri(v1_events, 'search')
        self._event_view = self.build_uri(v1_event, 'view')
        self._event_history = self.build_uri(v1_event, 'history')
        self._event_odds_summary = self.build_uri(v1_event, 'odds/summary')
        self._event_odds = self.build_uri(v1_event, 'odds')
        self._event_stats_trend = self.build_uri(v1_event, 'stats_trend')
        self._event_lineup = self.build_uri(v1_event, 'lineup')
        self._event_videos = self.build_uri(v1_events, 'videos')
        self._league = self.build_uri(v1_league, '')
        self._league_table = self.build_uri(v1_league, 'table')
        self._league_toplist = self.build_uri(v1_event, 'toplist')
        self._team = self.build_uri(v1_team, '')
        self._team_squad = self.build_uri(v1_team, 'squad')

    def inplay_events(self, sport_id,league_id=None):
        r"""InPlay Events  

        :param `sport_id`: (required),see [r-sportid](https://betsapi.com/docs/GLOSSARY.html#r-sportid) for more details.  
        :param `league_id`: (optional),useful when you want only one league.
        """

        params = {
            'sport_id': sport_id,
            'token': self.token
        }

        if league_id:
            params['league_id'] = league_id

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._inplay_events, params=params)
        return json.loads(req.content)

    def upcoming_events(self, sport_id, league_id=None, team_id=None, cc=None, day=None, page=None):
        r"""Upcoming Events  

        :param `sport_id`:(required),[R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid).  
        :param `league_id`:(optional),useful when you want only one league.   
        :param `team_id`:(optional),useful when you want only one team.   
        :param `cc`:(optional),Eg: 'co' for Colombia ([R-Countries](https://betsapi.com/docs/GLOSSARY.html#r-countries)).  
        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `page`:(optional),[R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager).  
        """
        params = {
            'sport_id': sport_id,
            'token': self.token
        }
        if league_id:
            params['league_id'] = league_id
        if team_id:
            params['team_id'] = team_id
        if cc:
            params['cc'] = cc
        if day:
            params['day'] = day
        if page:
            params['page'] = page

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._upcoming_events, params=params)
        return json.loads(req.content)

    def ended_events(self, sport_id, league_id=None, team_id=None, cc=None, day=None, page=None):
        r"""Ended Events  

        :param `sport_id`:(required),[R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid).  
        :param `league_id`:(optional),useful when you want only one league.   
        :param `team_id`:(optional),useful when you want only one team.   
        :param `cc`:(optional),Eg: 'co' for Colombia ([R-Countries](https://betsapi.com/docs/GLOSSARY.html#r-countries)).  
        :param `day`:(optional),format YYYYMMDD, eg: 20161201.  
        :param `page`:(optional),[R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager).  
        """
        params = {
            'sport_id': sport_id,
            'token': self.token
        }
        if league_id:
            params['league_id'] = league_id
        if team_id:
            params['team_id'] = team_id
        if cc:
            params['cc'] = cc
        if day:
            params['day'] = day
        if page:
            params['page'] = page

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._ended_events, params=params)
        return json.loads(req.content)

    def events_search(self, sport_id, home, away, time):
        r"""Events Search  
        Search for event with home/away name plus date.

        :param `sport_id`:(required),see [Reference](https://cn.betsapi.com/docs/events/search.html#sport_id) for more details.  
        :param `home`:(required),home team ID or name.  
        :param `away`:(required),away team ID or name.  
        :param `time`:(required),either UTC time epoch (Limited to 90 days) or day YYYYMMDD.  
        """
        params = {
            'sport_id': sport_id,
            'home': home,
            'away': away,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._events_search, params=params)
        return json.loads(req.content)

    def event_view(self, event_id):
        r"""Event View  

        :param `event_id`:(required),Event ID you get from events/*  .  
        you can send multiple event_ids in one request with event_id=1,2,3,4 up to max 10 ids.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_view, params=params)
        return json.loads(req.content)

    def event_history(self, event_id, qty=None):
        r"""Event History  
        History events of Home/Away Team before this event.
        
        :param `event_id`:(required),Event ID you get from events/*.  
        :param `qty`:(optional),default 10, allowing 1 to 20.  
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }
        if qty:
            params['qty'] = qty

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_history, params=params)
        return json.loads(req.content)

    def event_odds_summary(self, event_id):
        r"""Event Odds Summary  

        :param `event_id`:(required),Event ID you get from events/*.  
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_odds_summary, params=params)
        return json.loads(req.content)

    def event_odds(self, event_id, source=None, since_time=None, odds_market=None): 
        r"""Event Odds  

        :param `event_id`:(required),Event ID you get from events/*.   
        :param `source`:(optional),bet365, 10bet, ladbrokes, williamhill, betclic, pinnaclesports, planetwin365, ysb88, 188bet, unibet, bwin, betfair, betfred, cloudbet, betsson, betdaq, paddypower, sbobet, titanbet, betathome, dafabet, marathonbet, betvictor, intertops, betredkings, interwetten, betway, 1xbet, nitrogensports, winner, betregal, skybet, marsbet. defaults to bet365.  
        :param `since_time`:(optional),Integer. add_time will be >= $since_time in results. Faster to get only updates.  
        :param `odds_market`:(optional),String. if you only need one (or few) market to save time/bandwidth, pass the related string like &odds_market=1 or &odds_market=2,3 etc.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if source:
            params['source'] = source
        if since_time:
            params['since_time'] = since_time
        if odds_market:
            params['odds_market'] = odds_market

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_odds, params=params)
        return json.loads(req.content)

    def event_stats_trend(self, event_id):
        r"""Event Stats Trend  
        requires "Soccer Enhanced API" permission,see [Pricing](https://betsapi.com/mm/pricing) for more details.  
        Soccer only. only available for events after 2017-06-10.

        :param `event_id`:(required),Event ID you get from events/*.
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_stats_trend, params=params)
        return json.loads(req.content)

    def event_lineup(self, event_id):
        r"""Event Lineup  
        requires "Soccer Enhanced API" permission,see [Pricing](https://betsapi.com/mm/pricing) for more details.   
        Soccer only. Note not all events have lineup. you can get the flag (has_lineup) in /event/view.
        
        :param `event_id`:(required),Event ID you get from events/*.  
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }
        
        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_lineup, params=params)
        return json.loads(req.content)

    def event_videos(self, event_id):
        r"""Event Videos  
        NOTE: it's collected from Internet and not very reliable. The results might be wrong, USE IT at your own risk.
        
        :param `event_id`:(required),Event ID you get from events/*.          
        """
        params = {
            'event_id': event_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._event_videos, params=params)
        return json.loads(req.content)

    def league(self, sport_id, cc=None, page=None):
        r"""League

        :param sport_id:(required),see [R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid) for more details.  
        :param cc:(optional),Eg: 'co' for Colombia ([R-Countries](https://betsapi.com/docs/GLOSSARY.html#r-countries)).  
        :param page:(optional),[R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager).

        """
        params = {
            'sport_id': sport_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._league, params=params)
        return json.loads(req.content)

    def league_table(self, league_id):
        r"""League Table  
        Note a few of (less than 5%) teams do not have 'id'.

        :param  `league_id`:(required),flag 'has_leaguetable' from [League API](https://betsapi.com/docs/events/league_table.html#league).  
        """

        params = {
            'league_id': league_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._league_table, params=params)
        return json.loads(req.content)

    def league_toplist(self, league_id):
        r"""League TopList  
        requires "Soccer Enhanced API" permission,see [Pricing](https://betsapi.com/mm/pricing) for more details.  
        Note a few of (less than 5%) teams do not have 'id'.

        :param `league_id`:(required),flag 'has_toplist' from [League API](https://betsapi.com/docs/events/league_toplist.html#league).
        """
        params = {
            'league_id': league_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID


        req = requests.get(self._league_toplist, params=params)
        return json.loads(req.content)

    def team(self, sport_id, page=None):
        r"""Team  

        :prama `sport_id`:(required),see [R-SportID](https://betsapi.com/docs/GLOSSARY.html#r-sportid) for more details.  
        :prama `page`:(optional),see [R-Pager](https://betsapi.com/docs/GLOSSARY.html#r-pager) for more details.
        """
        params = {
            'sport_id': sport_id,
            'token': self.token
        }

        if page:
            params['page'] = page

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID

        req = requests.get(self._team, params=params)
        return json.loads(req.content)

    def team_squad(self, team_id):
        r"""Team Squad  
        requires "Soccer Enhanced API" permission,see [Pricing](https://betsapi.com/mm/pricing) for more details.
        
        :param `team_id`:(required),flag 'has_squad' from [Team API](https://betsapi.com/docs/events/team_squad.html#team).
        """
        params = {
            'team_id': team_id,
            'token': self.token
        }

        if self.LNG_ID:
            params['LNG_ID'] = self.LNG_ID
            
        req = requests.get(self._team_squad, params=params)
        return json.loads(req.content)
