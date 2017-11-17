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
import math
import random

# Execution environment for an event-based simulation. The passing of time is
# simulated by stepping from event to event.
ENV = simpy.Environment()

def main():
    """
    Call functions and alert the user as to what's going on.
    """
    bus_stop = BusStop(ENV, 19)
    # From 7:00 to 9:00 (2 hours)
    ENV.run(until=7201)
    bus_seats = simpy.Resource(ENV, capacity=30)

#weekday is a lowercase string whos value should be a day of the week, hours and minutes are integers would should be between 7:00 and 9:00 at 15 minute marks
def people_waiting(weekday,hours,minutes):
	
	if weekday=="monday" or weekday=="tuesday" or weekday=="wednesday" or weekday=="thursday":
		if hours==7 and minutes==0:
			mu=14
			sigma=4.58
		if hours==7 and minutes==15:
			mu=11.75
			sigma=3.4
		if hours==7 and minutes==30:
			mu=4.75
			sigma=0.96
		if hours==7 and minutes==45:
			mu=7.75
			sigma=2.22
		if hours==8 and minutes==0:
			mu=13.5
			sigma=1.29
		if hours==8 and minutes==15:
			mu=15.75
			sigma=2.75
		if hours==8 and minutes==30:
			mu=24
			sigma=2.16
		if hours==8 and minutes==45:
			mu=18
			sigma=5
		if hours==9 and minutes==0:
			mu=11.5
			sigma=0.71
	if weekday=="friday":
		if hours==7 and minutes==0:
			mu=4
			sigma=0.96
		if hours==7 and minutes==15:
			mu=1
			sigma=0.96
		if hours==7 and minutes==30:
			mu=3
			sigma=0.96
		if hours==7 and minutes==45:
			mu=4
			sigma=0.96
		if hours==8 and minutes==0:
			mu=3
			sigma=0.96
		if hours==8 and minutes==15:
			mu=8
			sigma=2.22
		if hours==8 and minutes==30:
			mu=10
			sigma=2.22
		if hours==8 and minutes==45:
			mu=7
			sigma=2.22
		if hours==9 and minutes==0:
			mu=16
			sigma=2.75
	x=random.gauss(mu, sigma)
	if x<0:
		x=0
	x=math.ceil(x)
	return(x)	
	
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
            # 1800 seconds == 30 minutes
            yield env.timeout(1800)

def bus(env, bus_stop, bus_seats):
    """
    """
    print('Bus arriving at %s' % env.now)
    # amount = gas_station.gas_tank.capacity - gas_station.gas_tank.level
    # yield gas_station.gas_tank.put(amount)
    yield env.timeout(1)

# If executed, run main()
if __name__ == '__main__':
    main()
