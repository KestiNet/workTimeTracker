#Converts decimal time to normal time
def convert_decimal_time(decima_time):
    hours = int(convert_decimal_time)
    minutes_decimal = (decima_time - hours) * 60
    minutes = round(minutes_decimal)
    return hours, minutes

#initialise a workTime array
workTime = []
#specify all workdays from Monday to Thursday
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]
# Asks user to enter time worked 
for weekday in weekdays:
    while True:
        try:
            decimal_time_input = float(input(f"Enter hours worked on {weekday}:"))
            break
        except ValueError:
            print("Invalid value, expecting a float")
    workTime.append(decimal_time_input)

#TODO add a function to ask user what time they started working on Friday so that the go home time can be calculated

#calls for the function that converts the decimal time
converter = convert_decimal_time(workTime)
normalConvert = sum(converter)
work_days_total = sum(workTime)

#prints out the values
print(f"total hours worked: ", dict(zip(weekdays, workTime)))
print(f"total hours worked: {work_days_total}")
print(f"total normal hours worked: {normalConvert}")