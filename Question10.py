from datetime import datetime

#10.1
def datetime_to_iso(x):
    return str(datetime(x[0],x[1],x[2],x[3],x[4],x[5]))

#10.2
def iso_to_datetime(x):
    try:
        return datetime.strptime(x,"%Y-%m-%d %H:%M:%S")
    except:
        print('Invalid date format!')

#10.3
def time_in_seconds(dt1,dt2):
    a = iso_to_datetime(dt1)
    b = iso_to_datetime(dt2)
    return (a-b).total_seconds()

date_time = datetime_to_iso((2021,12,25,10,20,30))
date_time_2 = datetime_to_iso((2021,11,10,12,31,23))

print('Date time in ISO format:',date_time)
print('Date time data:',iso_to_datetime(date_time_2))
print('Gap in seconds between 2 date times:',time_in_seconds(date_time,date_time_2))
