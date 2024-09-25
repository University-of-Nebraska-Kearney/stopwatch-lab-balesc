# Import Library
import datetime

#Seconds Per Hour
SECONDS_PER_HOUR = 3600
#Seconds per minute
SECONDS_PER_MINUTE = 60 

# Get time for start
input("Press Enter to start.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = start_time[0]
start_minute = start_time[1]
start_second = start_time[2]

# Get time for stop
input("Press Enter again to stop.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = stop_time[0]
stop_minute = stop_time[1]
stop_second = stop_time[2]

#Convert Time into Seconds only
startHour_seconds = SECONDS_PER_HOUR * int(start_hour) 
stopHour_seconds = SECONDS_PER_HOUR * int(stop_hour)
startMinute_seconds = SECONDS_PER_MINUTE * int(start_minute)
stopMinute_seconds = SECONDS_PER_MINUTE * int(stop_minute)

#add all the time together
total_secondsStart = int(startHour_seconds) + int(startMinute_seconds) + float(start_second)
total_secondsStop = int(stopHour_seconds) + int(stopMinute_seconds) + float(stop_second)

#Calculate the difference between stop seconds and start seconds
Seconds = total_secondsStop - total_secondsStart

#Calculate Hours, Seconds, and Minutes 
Hours = int(Seconds // SECONDS_PER_HOUR)
minutes = int(Seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
Seconds_elapsed = Seconds % SECONDS_PER_MINUTE

#print time in terminal
print(f'{Hours} : {minutes} : {Seconds_elapsed:.2f}')
