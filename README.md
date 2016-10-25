# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

Holden Oullette, hjo@uoregon.edu

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html

This project is a recreation of the calculator found at
https://rusa.org/octime_acp.html .  You can also use that calculator
to develop test data for the assertions in nosetest_acp_times.py

Brevet distance can be 200, 300, 400, 600, or 1000km. The first controle distance is always 0, and the last controle distance should be between the brevet distance and that distance plus 10%. A starting date and time is specified by the route designer. Input distances may be miles or kilometers (although brevet total distances are always one of the standard lengths in kilometers). For example, a 1000km brevet has a distance between 621.4 miles and 680 miles.
Locations may be optionally entered.

## Installation & Deployment

```bash
git clone https://github.com/TsFreddie/proj4-brevets.git
cd proj4-brevets
bash ./configure
make run
```

## Testing

```bash
make test
```

Alternatively, you can manually run nosetest_acp_times.py using
```bash
nosetests nosetest_acp_times.py
```
