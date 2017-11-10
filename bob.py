#!/usr/bin/env python3
"""
bob.py

Loop through every day and time slot in the week. At a given point in time, a
queue is filled with students waiting to get on the bus. A bus arrives and
the queue is emptied up until the bus reaches it's capacity. If there is
leftover students in the queue, then add them back in. Loop until time ends.
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
    bus_stop = BusStop(ENV, 19)
    ENV.run(until=15)

class BusStop():
    """
    """
    def __init__(self, env, num_in_line):
        self.queue = simpy.Resource(env, capacity=num_in_line)
        self.monitor_proc = env.process(self.monitor_line(env))

    def monitor_line(self, env):
        while True:
            print('Calling bus at %s' % env.now)
            env.process(bus(env, self))
            # 1800 seconds == 3 minutes
            yield env.timeout(1800)

def bus(env, bus_stop):
    """
    """
    print('Bus arriving at %s' % env.now)
    # amount = gas_station.gas_tank.capacity - gas_station.gas_tank.level
    # yield gas_station.gas_tank.put(amount)
    yield env.timeout(1800)
# If executed, run main()
if __name__ == '__main__':
    main()
