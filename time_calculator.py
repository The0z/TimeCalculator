# Function that adds time, takes two parameters and an optional one
def add_time(start, duration, start_day_of_week="off"):
    # Assume start times are valid times
    if start_day_of_week != "off":  # check if a day of week was given
        start_day_of_week = start_day_of_week.lower().capitalize()  # format
    start_hour = int(time_split(start, "hour"))
    start_min = int(time_split(start, "minute"))
    am_pm = time_split(start, "AMPM")
    if(am_pm == "PM"):    # correcting to 24 hour format
        start_hour += 12
    add_hour = int(time_split(duration, "hour"))
    add_min = int(time_split(duration, "minute"))

    new_24hours = start_hour + add_hour  # adding hours together
    new_mins = (start_min + add_min) % 60  # adding minutes together
    new_24hours += new_mins//60  # even though program assumes 60 mins max
    
    new_time = 0
    return new_time


# Takes in two parameters, returns time
def convert_time(time, h_or_m)

    return converted_time

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


def error_check(nums_ops):
    if len(nums_ops) != 3: #check for format
        return "Error: Input is Formatted incorrectly"
    # Check that correct operator used
    elif nums_ops[1] != "+" and nums_ops[1] != "-": #check for <60 minutes
        return "Error: Operator must be '+' or '-'."
    # Check it see if digits are numbers only
    elif not nums_ops[0].isdigit() or not nums_ops[2].isdigit(): #check for digits
        return "Error: Numbers must only contain digits."
    # Check to see if digit length greater than 4
    elif len(nums_ops[0]) > 4 or len(nums_ops[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
        return ""
