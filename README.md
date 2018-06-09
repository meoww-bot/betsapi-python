betsapi-python [![Build Status](https://travis-ci.org/qwqmeow/betsapi-python.svg)](https://travis-ci.org/qwqmeow/betsapi-python)
======

python SDK of betsapi.com.   
betsapi.com is a excellent api for bet app.

## Install
```
pip install betsapi
```
only support python2.7 temporarily.

## Example:
```py
from betsapi import *

token = 'YOUR-TOKEN'
bet365api = Bet365(token)

# set sport_id = '1'  to filter soccer sport
inplay_soccer = bet365api.inplay_filter('1')

# (optional) set language_id = 1,default English as language = '1'
bet365api.set_lng('1')

# set sport_id = '1' to view upcoming_events of soccer
bet365api.upcoming_events('1')
```
See [Docs](https://betsapi.com/docs/) for more details.

## Docs

https://betsapi.com/docs/

## gitbook

https://github.com/fayland/betsapi-gitbook

## translations

https://github.com/fayland/betsapi-translation/
