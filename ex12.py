import pyglet
import datetime

day = int(input("input the day"))
month = int(input("input the month"))
year = int(input("input the year"))

hour = int(input("input the hour"))
minute = int(input("input the minute"))
second = int(input("input the second"))
microsecond = int(input("input the microsecond"))

my_date = datetime.date(day=day, year= year, month=month)
print(my_date)
my_hour = datetime.time(hour=hour, minute=minute, second=second, microsecond = microsecond)
print(my_hour)
my_time = datetime.datetime.combine(my_date, my_hour)
print(type(my_time))

present_time = datetime.datetime.now()
print(type(present_time))
present_day = present_time.date()
# print(present_day)
present_hour = present_time.time()
# print(present_hour)
while True:
    if present_time == my_time:
        
        print("alarm")
    # music = pyglet.resource.media('26YARSREV1.wav')

    # music.play()
        # pyglet.app.run()
        break