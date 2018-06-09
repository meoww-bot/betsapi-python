#!/usr/bin/env python
#-*-coding:utf-8-*-

from betsapi import *

token = 'YOUR-TOKEN'
bet365api = Bet365(token)

eventsapi = Events(token)


def main():
    inplay_soccer = bet365api.inplay_filter('1')
    eventsapi.inplay_events('1')
    bet365api.upcoming_events('1')


if __name__ == '__main__':
    main()
