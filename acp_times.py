"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

# Speeds allowed in brevet, { distance: (minimum speed, maximum speed) }
SPEEDS = { 200: (15,34), 400: (15,32), 600: (15,30), 1000: (11.428,28), 1300: (13.333,26) }

# Time limits for brevet (24 hour time), { distance: (hour, minute)}
TIMES = { 200: (13,30), 300: (20,00), 400: (27,00), 600: (40,00), 1000: (75,00) }

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km < 0 or brevet_dist_km < 0:
        return "Please enter positive distance value"
    if control_dist_km > (brevet_dist_km * 1.1):
        #FIXME: do something
        print("hello")

    if control_dist_km >= brevet_dist_km:
        control_dist_km = brevet_dist_km

    time = math.modf(control_dist_km / SPEEDS[brevet_dist_km][1])
    hours = int(time[1])
    minutes = round(time[0] * 60)
    open_time = arrow.get(brevet_start_time).replace(hours=+hours, minutes=+minutes)

    return str(open_time)

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km < 0 or brevet_dist_km < 0:
        return 'Please enter positive distance value'
    if control_dist_km == 0:
        close_time = brevet_start_time.replace(hours=+1)
    elif control_dist_km >= brevet_dist_km:
        hours = TIMES[brevet_dist_km][0]
        minutes = TIMES[brevet_dist_km][1]
        close_time = brevet_start_time.replace(hours=+hours, minutes=+minutes)
    else:
        time = math.modf(control_dist_km / SPEEDS[brevet_dist_km][0])
        hours = int(time[1])
        minutes = round(time[0] * 60)
        close_time = arrow.get(brevet_start_time).replace(hours=+hours, minutes=+minutes)

    return str(close_time)