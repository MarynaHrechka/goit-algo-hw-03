from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d") # format "2024-01-22"
    except ValueError as e:
        print('wrong date format')
        return
    diff = datetime.today() - datetime_object
    return diff.days
