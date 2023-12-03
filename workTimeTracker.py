from datetime import datetime, timedelta

def convert_decimal_time(decimal_time):
    hours = int(decimal_time)
    minutes_decimal = (decimal_time - hours) * 60
    minutes = round(minutes_decimal)
    return hours, minutes

def calculate_end_time(start_time, total_hours):
    start_datetime = datetime.strptime(start_time, "%H:%M")
    end_datetime = start_datetime + timedelta(hours=total_hours)
    return end_datetime.strftime("%H:%M")

workTime = []

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]

for weekday in weekdays:
    while True:
        try:
            decimal_time_input = float(input(f"Enter hours worked on {weekday}: "))
            break
        except ValueError:
            print("Invalid value, expecting a float")
    workTime.append(decimal_time_input)

# Ask for the start time on Friday
start_time_friday = input("Enter the start time on Friday (HH:MM): ")

# Calculate the remaining hours needed to reach the target
remaining_hours = 41 - sum(workTime)

# Calculate the end time on Friday
end_time_friday = calculate_end_time(start_time_friday, remaining_hours)

converter = [convert_decimal_time(decimal_time) for decimal_time in workTime]

# Extract hours and minutes from the converter list
hours_list, minutes_list = zip(*converter)

# Calculate total hours and total minutes
total_hours = sum(hours_list) + remaining_hours
total_minutes = sum(minutes_list)

# Convert total minutes to hours and minutes
total_hours += total_minutes // 60
total_minutes %= 60

print("Total hours worked per day:", dict(zip(weekdays, workTime)))
print("Total hours worked in decimal format:", workTime)
print(f"Total hours worked: {total_hours} hours and {total_minutes} minutes")

# Print the end time on Friday
print(f"If you start working on Friday at {start_time_friday}, you can leave at {end_time_friday}.")
