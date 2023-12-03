def convert_decimal_time(decima_time):
    hours = int(convert_decimal_time)
    minutes_decimal = (decima_time - hours) * 60
    minutes = round(minutes_decimal)
    return hours, minutes

workTime = []

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for weekday in weekdays:
    while True:
        try:
            decimal_time_input = float(input(f"Enter hours worked on {weekday}:"))
            break
        except ValueError:
            print("Invalid value, expecting a float")
    workTime.append(decimal_time_input)

converter = convert_decimal_time(workTime)
normalConvert = sum(converter)
work_days_total = sum(workTime)


print(f"total hours worked: ", dict(zip(weekdays, workTime)))
print(f"total hours worked: {work_days_total}")
print(f"total normal hours worked: {normalConvert}")