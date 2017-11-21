#!/usr/bin/env python
"""
bob_two.py

This is Bob 2.0

We rolled our own simulation framework because you only live once.
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Python std. lib. imports
import math
import random

def main():
    """
    Loop through every day of the week + bus arrival time. Calculate the number
    of people waiting and how many are left behind, and print a status update.
    """
    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    bus_arrival_times = [
        (7, 0), (7, 15), (7, 30), (7, 45),
        (8, 0), (8, 15), (8, 30), (8, 45),
        (9, 0)
    ]
    for day_of_the_week in days_of_the_week:
        left_behind = 0
        for bus_arrival_time in bus_arrival_times:
            number_waiting = people_waiting(day_of_the_week,
                                            bus_arrival_time[0],
                                            bus_arrival_time[1])
            number_waiting += left_behind
            if(number_waiting > 30):
                left_behind = number_waiting - left_behind
            print("{} people were at the bus stop at {}:{} on {}, {} weren't able to get on the bus".format(number_waiting,
                                                                                                            bus_arrival_time[0],
                                                                                                            bus_arrival_time[1],
                                                                                                            day_of_the_week,
                                                                                                            left_behind))

def people_waiting(weekday, hours, minutes):
    """
    Helper function to determine the number of people waiting at the bus stop
    for a given date and time. Friday is different. Assign a mu and sigma that
    get plugged into a gaussian distribution. Return the ceil of the value
    returned from the distribution.
    """
    if weekday in ["monday", "tuesday", "wednesday", "thursday"]:
        if hours == 7 and minutes == 0:
            mu = 14
            sigma = 4.58
        elif hours == 7 and minutes == 15:
            mu = 11.75
            sigma = 3.4
        elif hours == 7 and minutes == 30:
            mu = 4.75
            sigma = 0.96
        elif hours == 7 and minutes == 45:
            mu = 7.75
            sigma = 2.22
        elif hours == 8 and minutes == 0:
            mu = 13.5
            sigma = 1.29
        elif hours == 8 and minutes == 15:
            mu = 15.75
            sigma = 2.75
        elif hours == 8 and minutes == 30:
            mu = 24
            sigma = 2.16
        elif hours == 8 and minutes == 45:
            mu = 18
            sigma = 5
        elif hours == 9 and minutes == 0:
            mu = 11.5
            sigma = 0.71
    else:
        if hours == 7 and minutes == 0:
            mu = 4
            sigma = 0.96
        elif hours == 7 and minutes == 15:
            mu = 1
            sigma = 0.96
        elif hours == 7 and minutes == 30:
            mu = 3
            sigma = 0.96
        elif hours == 7 and minutes == 45:
            mu = 4
            sigma = 0.96
        elif hours == 8 and minutes == 0:
            mu = 3
            sigma = 0.96
        elif hours == 8 and minutes == 15:
            mu = 8
            sigma = 2.22
        elif hours == 8 and minutes == 30:
            mu = 10
            sigma = 2.22
        elif hours == 8 and minutes == 45:
            mu = 7
            sigma = 2.22
        elif hours == 9 and minutes == 0:
            mu = 16
            sigma = 2.75
    gaussian_distribution_value = random.gauss(mu, sigma)
    if gaussian_distribution_value < 0:
        return 0
    else:
        return math.ceil(gaussian_distribution_value)

# If executed, run main()
if __name__ == '__main__':
    main()
