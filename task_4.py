from datetime import datetime, timedelta


FRIDAY = 4
DATE_PATTERN = "%Y.%m.%d"
OPERATION_DAYS = range(0, 7)


def get_upcoming_birthdays(users: list) -> list:
    result = []
    today = datetime.today().date()
    for user in users:
        birthday = datetime.strptime(user["birthday"], DATE_PATTERN).date()
        birthday_this_year = datetime(year=today.year, month=birthday.month, day=birthday.day)
        time_delta = birthday_this_year.date() - today
        if time_delta.days in OPERATION_DAYS:
            congratulation_offset = timedelta(7 - birthday_this_year.weekday()) if birthday_this_year.weekday() > FRIDAY else timedelta(days=0)
            congratulation_date = birthday_this_year + congratulation_offset
            result.append(dict(name=user["name"], congratulation_date=congratulation_date.strftime(DATE_PATTERN)))
    return result
