"""
Nose Tests
Assertion data from https://rusa.org/octime_acp.html
"""

import arrow
from acp_times import *

def test():
    assert open_time(0,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:00:00+00:00'
    assert close_time(0,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T01:00:00+00:00'

    assert open_time(1,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:02:00+00:00'
    assert close_time(1,   200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T00:04:00+00:00'

    assert open_time(50,  200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T01:28:00+00:00'
    assert close_time(50,  200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T03:20:00+00:00'

    assert open_time(100, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T02:56:00+00:00'
    assert close_time(100, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T06:40:00+00:00'

    assert open_time(200, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T05:53:00+00:00'
    assert close_time(200, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T13:30:00+00:00'

    assert open_time(201, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T05:53:00+00:00'
    assert close_time(201, 200, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T13:30:00+00:00'

test() #so it can be run from the commandline as well
