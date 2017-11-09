#!/usr/bin/env python
"""
bob.py
"""
# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Third party imports
import simpy

# Execution environment for an event-based simulation. The passing of time is
# simulated by stepping from event to event.
ENV = simpy.Environment()

def main():
    """
    Call functions and alert the user as to what's going on.
    """
    ENV.process(car(ENV))
    ENV.run(until=15)

def car(environ):
    while True:
        print('Start parking at %d' % environ.now)
        parking_duration = 5
        yield environ.timeout(parking_duration)

        print('Start driving at %d' % environ.now)
        trip_duration = 2
        yield environ.timeout(trip_duration)

# If executed, run main()
if __name__ == '__main__':
    main()
