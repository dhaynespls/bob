import math
import random

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

def  bus():
	day='monday'
	if(day=="monday"):
		I=people_waiting("monday",7,0)
		IM=0
		if(I>30):
			IM=I-IM
		print("{} people were at the bus stop at 7:00 on monday, {} weren't able to get on bus".format(I,IM))
		
		II=people_waiting("monday",7,15)+IM
		IIM=0
		if(II>30):
			IIM=II-IIM
		print("{} people were at the bus stop at 7:15 on monday, {} weren't able to get on bus".format(II,IIM))
		
		III=people_waiting("monday",7,30)+IIM
		IIIM=0
		if(III>30):
			IIIM=III-IIIM
		print("{} people were at the bus stop at 7:30 on monday, {} weren't able to get on bus".format(III,IIIM))
		
		IV=people_waiting("monday",7,45)+IIIM
		IVM=0
		if(IV>30):
			IVM=IV-IVM
		print("{} people were at the bus stop at 7:45 on monday, {} weren't able to get on bus".format(IV,IVM))
		
		V=people_waiting("monday",8,0)+IVM
		VM=0
		if(V>30):
			VM=V-VM
		print("{} people were at the bus stop at 8:00 on monday, {} weren't able to get on bus".format(V,VM))
		
		VI=people_waiting("monday",8,15)+VM
		VIM=0
		if(VI>30):
			VIM=VI-VIM
		print("{} people were at the bus stop at 8:15 on monday, {} weren't able to get on bus".format(VI,VIM))
		
		VII=people_waiting("monday",8,30)+VIM
		VIIM=0
		if(VII>30):
			VIIM=VII-VIIM
		print("{} people were at the bus stop at 8:30 on monday, {} weren't able to get on bus".format(VII,VIIM))
		
		VIII=people_waiting("monday",8,45)+VIIM
		VIIIM=0
		if(VIII>30):
			VIIIM=VIII-VIIIM
		print("{} people were at the bus stop at 8:45 on monday, {} weren't able to get on bus".format(VIII,VIIIM))
		
		IX=people_waiting("monday",9,0)+VIIIM
		IXM=0
		if(IX>30):
			IXM=IX-IXM
		print("{} people were at the bus stop at 9:00 on monday, {} weren't able to get on bus".format(IX,IXM))
		
		
		
	day="tuesday"	
	if(day=="tuesday"):
		I=people_waiting("tuesday",7,0)
		IM=0
		if(I>30):
			IM=I-IM
		print("{} people were at the bus stop at 7:00 on tuesday, {} weren't able to get on bus".format(I,IM))
		
		II=people_waiting("tuesday",7,15)+IM
		IIM=0
		if(II>30):
			IIM=II-IIM
		print("{} people were at the bus stop at 7:15 on tuesday, {} weren't able to get on bus".format(II,IIM))
		
		III=people_waiting("tuesday",7,30)+IIM
		IIIM=0
		if(III>30):
			IIIM=III-IIIM
		print("{} people were at the bus stop at 7:30 on tuesday, {} weren't able to get on bus".format(III,IIIM))
		
		IV=people_waiting("tuesday",7,45)+IIIM
		IVM=0
		if(IV>30):
			IVM=IV-IVM
		print("{} people were at the bus stop at 7:45 on tuesday, {} weren't able to get on bus".format(IV,IVM))
		
		V=people_waiting("tuesday",8,0)+IVM
		VM=0
		if(V>30):
			VM=V-VM
		print("{} people were at the bus stop at 8:00 on tuesday, {} weren't able to get on bus".format(V,VM))
		
		VI=people_waiting("tuesday",8,15)+VM
		VIM=0
		if(VI>30):
			VIM=VI-VIM
		print("{} people were at the bus stop at 8:15 on tuesday, {} weren't able to get on bus".format(VI,VIM))
		
		VII=people_waiting("tuesday",8,30)+VIM
		VIIM=0
		if(VII>30):
			VIIM=VII-VIIM
		print("{} people were at the bus stop at 8:30 on tuesday, {} weren't able to get on bus".format(VII,VIIM))
		
		VIII=people_waiting("tuesday",8,45)+VIIM
		VIIIM=0
		if(VIII>30):
			VIIIM=VIII-VIIIM
		print("{} people were at the bus stop at 8:45 on tuesday, {} weren't able to get on bus".format(VIII,VIIIM))
		
		IX=people_waiting("tuesday",9,0)+VIIIM
		IXM=0
		if(IX>30):
			IXM=IX-IXM
		print("{} people were at the bus stop at 9:00 on tuesday, {} weren't able to get on bus".format(IX,IXM))
		
	day="wednesday"	
	if(day=="wednesday"):
		I=people_waiting("wednesday",7,0)
		IM=0
		if(I>30):
			IM=I-IM
		print("{} people were at the bus stop at 7:00 on wednesday, {} weren't able to get on bus".format(I,IM))
		
		II=people_waiting("wednesday",7,15)+IM
		IIM=0
		if(II>30):
			IIM=II-IIM
		print("{} people were at the bus stop at 7:15 on wednesday, {} weren't able to get on bus".format(II,IIM))
		
		III=people_waiting("wednesday",7,30)+IIM
		IIIM=0
		if(III>30):
			IIIM=III-IIIM
		print("{} people were at the bus stop at 7:30 on wednesday, {} weren't able to get on bus".format(III,IIIM))
		
		IV=people_waiting("wednesday",7,45)+IIIM
		IVM=0
		if(IV>30):
			IVM=IV-IVM
		print("{} people were at the bus stop at 7:45 on wednesday, {} weren't able to get on bus".format(IV,IVM))
		
		V=people_waiting("wednesday",8,0)+IVM
		VM=0
		if(V>30):
			VM=V-VM
		print("{} people were at the bus stop at 8:00 on wednesday, {} weren't able to get on bus".format(V,VM))
		
		VI=people_waiting("wednesday",8,15)+VM
		VIM=0
		if(VI>30):
			VIM=VI-VIM
		print("{} people were at the bus stop at 8:15 on wednesday, {} weren't able to get on bus".format(VI,VIM))
		
		VII=people_waiting("wednesday",8,30)+VIM
		VIIM=0
		if(VII>30):
			VIIM=VII-VIIM
		print("{} people were at the bus stop at 8:30 on wednesday, {} weren't able to get on bus".format(VII,VIIM))
		
		VIII=people_waiting("wednesday",8,45)+VIIM
		VIIIM=0
		if(VIII>30):
			VIIIM=VIII-VIIIM
		print("{} people were at the bus stop at 8:45 on wednesday, {} weren't able to get on bus".format(VIII,VIIIM))
		
		IX=people_waiting("wednesday",9,0)+VIIIM
		IXM=0
		if(IX>30):
			IXM=IX-IXM
		print("{} people were at the bus stop at 9:00 on wednesday, {} weren't able to get on bus".format(IX,IXM))
		
	day="thursday"	
	if(day=="thursday"):
		I=people_waiting("thursday",7,0)
		IM=0
		if(I>30):
			IM=I-IM
		print("{} people were at the bus stop at 7:00 on thursday, {} weren't able to get on bus".format(I,IM))
		
		II=people_waiting("thursday",7,15)+IM
		IIM=0
		if(II>30):
			IIM=II-IIM
		print("{} people were at the bus stop at 7:15 on thursday, {} weren't able to get on bus".format(II,IIM))
		
		III=people_waiting("thursday",7,30)+IIM
		IIIM=0
		if(III>30):
			IIIM=III-IIIM
		print("{} people were at the bus stop at 7:30 on thursday, {} weren't able to get on bus".format(III,IIIM))
		
		IV=people_waiting("thursday",7,45)+IIIM
		IVM=0
		if(IV>30):
			IVM=IV-IVM
		print("{} people were at the bus stop at 7:45 on thursday, {} weren't able to get on bus".format(IV,IVM))
		
		V=people_waiting("thursday",8,0)+IVM
		VM=0
		if(V>30):
			VM=V-VM
		print("{} people were at the bus stop at 8:00 on thursday, {} weren't able to get on bus".format(V,VM))
		
		VI=people_waiting("thursday",8,15)+VM
		VIM=0
		if(VI>30):
			VIM=VI-VIM
		print("{} people were at the bus stop at 8:15 on thursday, {} weren't able to get on bus".format(VI,VIM))
		
		VII=people_waiting("thursday",8,30)+VIM
		VIIM=0
		if(VII>30):
			VIIM=VII-VIIM
		print("{} people were at the bus stop at 8:30 on thursday, {} weren't able to get on bus".format(VII,VIIM))
		
		VIII=people_waiting("thursday",8,45)+VIIM
		VIIIM=0
		if(VIII>30):
			VIIIM=VIII-VIIIM
		print("{} people were at the bus stop at 8:45 on thursday, {} weren't able to get on bus".format(VIII,VIIIM))
		
		IX=people_waiting("thursday",9,0)+VIIIM
		IXM=0
		if(IX>30):
			IXM=IX-IXM
		print("{} people were at the bus stop at 9:00 on thursday, {} weren't able to get on bus".format(IX,IXM))
		
		
	day="friday"	
	if(day=="friday"):
		I=people_waiting("friday",7,0)
		IM=0
		if(I>30):
			IM=I-IM
		print("{} people were at the bus stop at 7:00 on friday, {} weren't able to get on bus".format(I,IM))
		
		II=people_waiting("friday",7,15)+IM
		IIM=0
		if(II>30):
			IIM=II-IIM
		print("{} people were at the bus stop at 7:15 on friday, {} weren't able to get on bus".format(II,IIM))
		
		III=people_waiting("friday",7,30)+IIM
		IIIM=0
		if(III>30):
			IIIM=III-IIIM
		print("{} people were at the bus stop at 7:30 on friday, {} weren't able to get on bus".format(III,IIIM))
		
		IV=people_waiting("friday",7,45)+IIIM
		IVM=0
		if(IV>30):
			IVM=IV-IVM
		print("{} people were at the bus stop at 7:45 on friday, {} weren't able to get on bus".format(IV,IVM))
		
		V=people_waiting("friday",8,0)+IVM
		VM=0
		if(V>30):
			VM=V-VM
		print("{} people were at the bus stop at 8:00 on friday, {} weren't able to get on bus".format(V,VM))
		
		VI=people_waiting("friday",8,15)+VM
		VIM=0
		if(VI>30):
			VIM=VI-VIM
		print("{} people were at the bus stop at 8:15 on friday, {} weren't able to get on bus".format(VI,VIM))
		
		VII=people_waiting("friday",8,30)+VIM
		VIIM=0
		if(VII>30):
			VIIM=VII-VIIM
		print("{} people were at the bus stop at 8:30 on friday, {} weren't able to get on bus".format(VII,VIIM))
		
		VIII=people_waiting("friday",8,45)+VIIM
		VIIIM=0
		if(VIII>30):
			VIIIM=VIII-VIIIM
		print("{} people were at the bus stop at 8:45 on friday, {} weren't able to get on bus".format(VIII,VIIIM))
		
		IX=people_waiting("friday",9,0)+VIIIM
		IXM=0
		if(IX>30):
			IXM=IX-IXM
		print("{} people were at the bus stop at 9:00 on friday, {} weren't able to get on bus".format(IX,IXM))
bus()
