SECONDS_DAY = 86400
SECONDS_HOUR = 3600
SECONDS_MINUTE = 60

seconds = int(input("Enter the number of seconds: "))
if seconds >= SECONDS_DAY:
    days = seconds // SECONDS_DAY
    seconds = seconds % SECONDS_DAY
    print("Days: ", days)

if seconds >= SECONDS_HOUR:
    hours = seconds // SECONDS_HOUR
    seconds = seconds % SECONDS_HOUR
    print("Hours: ", hours)

if seconds >= SECONDS_MINUTE:
    minutes = seconds // SECONDS_MINUTE
    seconds = seconds % SECONDS_MINUTE
    print("Minutes: ", minutes)

print("Seconds: ", seconds)
