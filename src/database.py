import csv
from src.reminder import PoliteReminder
from src.deadlined_reminders import DateReminder

def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text):

    with open('reminders.csv', 'a+', newline='\n') as file:
        reminder = PoliteReminder(text) 
        writer = csv.writer(file)
        writer.writerow([reminder.text])
