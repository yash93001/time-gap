from datetime import timedelta


def convert_time(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]

    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]

    else:
        return str(int(time[:2]) + 12) + time[2:8]


if __name__ == '__main__':
    time_1 = str(input('enter the first time in am/pm format\n'))
    time_2 = str(input('enter the second time in am/pm format\n'))

    time_1_converted = convert_time(time_1)
    time_2_converted = convert_time(time_2)

    hour1 = time_1_converted[:2]
    min1 = time_1_converted[3:-4]
    sec1 = time_1_converted[6:]

    hour2 = time_2_converted[:2]
    min2 = time_2_converted[3:-4]
    sec2 = time_2_converted[6:]
    time1 = int(hour1) * 60 * 60 + int(min1) * 60 + int(sec1)
    time2 = int(hour2) * 60 * 60 + int(min2) * 60 + int(sec2)
    difference = abs(time1 - time2)

    print(f"difference in seconds {difference}\n")
    print(f"difference in time format {timedelta(seconds= difference)}")
