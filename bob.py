#!/bin/sh python
"""
bob.py
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import simpy

def main():
    """
    Call functions and alert the user as to what's going on.
    """
    env = simpy.Environment()
    env.process(car(env))
    env.run(until=15)

def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 5
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)


# If executed, run main()
if __name__ == '__main__':
    main()
