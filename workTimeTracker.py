workTime = []

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for weekday in weekdays:
    while True:
        try:
            float_input = float(input(f"Enter hours worked on {weekday}:"))
            break
        except ValueError:
            print("Invalid value, expecting a float")
    workTime.append(float_input)

work_days_total = sum(workTime)

print(f"total hours worked: ", dict(zip(weekdays, workTime)))
print(f"total hours worked: {work_days_total}")
