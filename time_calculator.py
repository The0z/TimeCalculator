# Function that adds time, takes two parameters and an optional one
def add_time(start, duration, starting_day="off"):
    # Assume start times are valid times
    if starting_day != "off":  # check if a day of week was given
        starting_day = starting_day.lower().capitalize()  # format
    start_hour = int(time_split(start, "hour"))
    start_min = int(time_split(start, "minute"))
    am_pm = time_split(start, "AMPM")
    if(am_pm == "PM"):    # correcting to 24 hour format
        start_hour += 12
    add_hour = int(time_split(duration, "hour"))
    add_min = int(time_split(duration, "minute"))

    new_24hours = start_hour + add_hour  # adding hours together
    new_mins = (start_min + add_min) % 60  # adding minutes together
    new_24hours += (start_min + add_min) // 60  # adding extra hours if min>60

    single_day_hour = new_24hours % 24
    new_days = new_24hours // 24

    # converting to 12 hour clock
    if(single_day_hour <= 11):
        new_am_pm = "AM"
        if(single_day_hour == 0):  # 12 am case
            single_day_hour = 12
    elif(single_day_hour > 11):
        new_am_pm = "PM"
        if(single_day_hour > 12):  # when time is > 12 PM.
            single_day_hour += -12

    # if logic to handle mins less than 10. (i.e. proper formatting)
    if new_mins == 0:  # adding another 0 incase minutes is 0 i.e.) 0 -> 00
        new_mins = str(new_mins) + "0"
    elif new_mins < 10:
        new_mins = "0" + str(new_mins)

    # updating new time
    new_time = str(single_day_hour) + ":" + str(new_mins) + " "\
        + str(new_am_pm) + days_later(new_days, starting_day)
    return new_time


def days_later(days, starting_day):
    name_of_day = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
                   "Friday": 4, "Saturday": 5, "Sunday": 6}
    int_of_day = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                  4: "Friday", 5: "Saturday", 6: "Sunday"}

    if starting_day != "off":
        new_day_int = (days + int(name_of_day.get(starting_day))) % 7
        new_day_name = ", " + int_of_day.get(new_day_int)
    else:
        new_day_name = ""  # empty string is inserted if starting day not given

    # formatting text if else logic
    if days == 0:
        return new_day_name  # i.e. Monday or Blank if Starting day off
    elif days == 1:
        return new_day_name + " (next day)"  # i.e. monday (next day)
    else:
        return new_day_name + " (" + str(days) + " days later)"


def time_split(h_m_AMPM, part_required):
    time = h_m_AMPM.split(":")
    hour = time[0]
    min_AMPM = time[1].split(" ")

    if(part_required == "hour"):
        return hour
    elif(part_required == "minute"):
        return min_AMPM[0]
    elif(part_required == "AMPM"):
        return min_AMPM[1]
    else:
        return "Error in Time Split Function"
