# Main function receives start time (AM/PM), duration and optionally the day
def add_time(start, duration, day=""):
    # Function that exchanges PM to AM and vice versa
    def change_APM(APM):
        if APM == "PM":
            return "AM"
        elif APM == "AM":
            return "PM"        
    # Function to handle passing of days when duration is big enough
    # Function to be called when there's a change of day, therefore "crosses" shall never be zero
    def change_day(day, crosses, PM=False):
        days = {
            "SUNDAY": 1, 
            "MONDAY": 2,
            "TUESDAY": 3,
            "WEDNESDAY": 4,
            "THURSDAY": 5,
            "FRIDAY": 6,
            "SATURDAY": 7
        }
        if PM == False:
            ref = days[day.upper()] + crosses // 2
        elif  PM == True:
            ref = days[day.upper()] + crosses // 2 + crosses % 2
        if ref > 7:
            ref = ref % 7
        return list(days.keys())[list(days.values()).index(ref)].title()

#### Processing input data ####
    # Transforming the start time in suitable programming entities
    start_hours, rest = start.split(":")
    start_minutes, start_APM = rest.split(" ")
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)

    # Transforming the duration in suitable programming entities
    duration_hours, duration_minutes = int(duration.split(":")[0]), int(duration.split(":")[1])

    # Managing minutes addition 
    new_minutes = start_minutes + duration_minutes
    if new_minutes >= 60:
        duration_hours += 1
        new_minutes = new_minutes%60
    
    # Managing hours addition
    new_hour = start_hours + duration_hours
    crosses_threshold = new_hour // 12
    if crosses_threshold % 2 == 1:
        end_APM = change_APM(start_APM)
    else:
        end_APM = start_APM
    new_hour = new_hour%12
    if new_hour == 0:
        new_hour = 12

#### Displaying processed data #### 
    # When optional chosen weekday is turned off
    if day == "":
        # No change AM/PM
        if crosses_threshold == 0:
            new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM
        # When changes AM/PM and starts at PM
        elif start_APM == "PM":
            # Case of 1 day duration
            if crosses_threshold < 3:
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + " (next day)"
            # Case of more days duration
            else:
                n = crosses_threshold // 2 + crosses_threshold % 2
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + f' ({n} days later)'
        # When changes AM/PM and starts at AM
        elif start_APM == "AM":
            # AM to PM on the same day
            if crosses_threshold == 1:
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM 
            # case of 1 day duration
            elif crosses_threshold < 4:
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + " (next day)"
            # Case of more days duration
            else:
                n = crosses_threshold // 2 
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + f' ({n} days later)'
    # When optional chosen weekday is given
    else:
        # No change AM/PM
        if crosses_threshold == 0:
            new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + ", " + day.title()
        # When changes AM/PM and starts at PM
        elif start_APM == "PM":
            # Case of 1 day duration
            if crosses_threshold < 3:
                new_day = change_day(day, crosses_threshold, True)
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + f", {new_day}" + " (next day)"
            # Case of more days duration
            else:
                new_day = change_day(day, crosses_threshold, True)
                n = crosses_threshold // 2 + crosses_threshold % 2
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + f', {new_day}' + f' ({n} days later)'
        # When changes AM/PM and starts at AM
        elif start_APM == "AM":
            # AM to PM on the same day
            if crosses_threshold == 1:
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + ", " + day.title()
            # case of 1 day duration
            elif crosses_threshold < 4:
                new_day = change_day(day, crosses_threshold)
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + f", {new_day}" + " (next day)"
            # Case of more days duration
            else:
                new_day = change_day(day, crosses_threshold) 
                n = crosses_threshold // 2 
                new_time = str(new_hour) + ":" + str(new_minutes).zfill(2) + " " + end_APM + f', {new_day}' + f' ({n} days later)'
    
    return new_time

