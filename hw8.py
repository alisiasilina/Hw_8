from datetime import datetime, timedelta

users = [
    {"name": "Viktoria", "birthday": "17.06.2000"},
    {"name": "Maxim", "birthday": "19.06.1992"},
    {"name": "Anna", "birthday": "5.03.1998"},
    {"name": "Maria", "birthday": "26.08.1987"},
    {"name": "Anton", "birthday": "11.12.2003"},
    {"name": "Daniil", "birthday": "9.02.2001"},
    {"name": "Valeria", "birthday": "22.07.1999"}
]


def get_birthdays_per_week(users):
    weekday = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next Monday': ''
        }
    start = datetime.now().date()
    end = start + timedelta(days=7)
    for i in users:
        birthday = datetime.strptime(i["birthday"], "%d.%m.%Y")
        date_b = datetime(start.year, birthday.month, birthday.day)
        if start <= date_b.date() <= end:
            day = date_b.weekday()
            if day == 0:
                weekday['Monday'] += i['name']
            if day == 1:
                weekday['Tuesday'] += i['name']
            if day == 2:
                weekday['Wednesday'] += i['name']
            if day == 3:
                weekday['Thursday'] += i['name']
            if day == 4:
                weekday['Friday'] += i['name']
            if day in (5, 6):
                weekday['Next Monday'] += i['name']

    for k, v in weekday.items():
        count = 0
        if len(v) > 0:
            print(k + ': ' + v)
        else:
            count += 1
    if count > 0:
        print("No birthdays")

 
print(get_birthdays_per_week(users))         
