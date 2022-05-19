import time
import questionary
from datetime import datetime
from num2words import num2words


def parse_datetime(date, time):
    dt = date + " " + time
    datetime_object = datetime.strptime(dt, '%d.%m.%Y %H:%M')
    return datetime_object


def is_now(now, dt):
    diff = (now - dt).total_seconds()
    if diff >= 30:
        return 'past'
    if diff < -30:
        return 'future'
    return 'now'

def results(dt, i):
    strdate = datetime.strftime(dt, '%d.%m.%Y - %H:%M')
    ord = num2words(i + 1, to='ordinal')
    return f"The { ord } date has been reached! ({ strdate })"


def main():
    num = questionary.text("How much data do you want to enter?").ask()
    num = int(num)


    reminders = []

    while num > 0 :
        date = questionary.text("Please enter a date (DD.MM.YYYY):").ask()
        time_str = questionary.text("Please enter a time (HH:MM):").ask()
        datetime_object = parse_datetime(date, time_str)
        reminders.append(datetime_object)
        print()
        num = num - 1


    print("Thank you very much. I will notify them!\n...")

    reminders.sort()

    for i, dt in enumerate(reminders):
        
        while True:
            now = datetime.now()
            w = is_now(now, dt)
            if w == 'past' or w == 'now':
                break
            else:
                time.sleep(60)

        
        print(results(dt, i))
        
    
if __name__ == "__main__":
    main()