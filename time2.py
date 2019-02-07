#Benjamin Page
#2/7/2019
#Found issue with improperly-matched variable wait_time (was wai_time)
str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
