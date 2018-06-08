# -*- coding: utf-8 -*-
"""
BetsAPI library
"""
__version__ = '1.0.0'

from .bet365 import Bet365
from .betfair import Betfair
from .betway import Betway
from .bwin import BWin
from .events import Events
from .results import Results
from .sbobet import Sbobet

__all__ = ("Bet365", "Betfair", "Betway","BWin","Events","Results","Sbobet")
