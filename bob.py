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
    """
    For the entire duration of the simulation run, the car process will park
    for 5 second intervals and drive for 2 second intervals. Driving can only
    occur after parking has completed.
    """
    while True:
        # Parking
        print('Start parking at %d' % environ.now)
        parking_duration = 5
        # Time out for the provided duration, then continue
        yield environ.timeout(parking_duration)

        # Driving
        print('Start driving at %d' % environ.now)
        trip_duration = 2
        # Time out for the provided duration, then continue
        yield environ.timeout(trip_duration)

# If executed, run main()
if __name__ == '__main__':
    main()
