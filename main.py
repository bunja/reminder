import time
import questionary
from datetime import datetime
from num2words import num2words



num = questionary.text("How much data do you want to enter?").ask()
num = int(num)


reminders = []

while num > 0 :
    date = questionary.text("Please enter a date (DD.MM.YYYY):").ask()
    time = questionary.text("Please enter a time (HH:MM):").ask()
    dt = date + " " + time
    datetime_object = datetime.strptime(dt, '%d.%m.%Y %H:%M')
    reminders.append(datetime_object)
    print()
    num = num - 1


print("Thank you very much. I will notify them!\n...")

reminders.sort()

for i, dt in enumerate(reminders):
    
    while True:
        now = datetime.datetime.now()
        diff = abs((now - dt).total_seconds())
        if diff <= 60:
            break
        else:
            time.sleep(60)

    strdate = datetime.strftime(dt, '%d.%m.%Y - %H:%M')
    ord = num2words(i + 1, to='ordinal')
    print(f"The { ord } date has been reached! ({ strdate })")