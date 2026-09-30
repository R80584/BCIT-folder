import dow
def getDayOfTheWeekForUserDate():
    year = int(input("Enter a year (e.g. 2019): "))
    month = int(input("Enter a month (1-12): "))
    day = int(input("Enter a day (1-31): "))
    weekday = dow.getDayOfTheWeek(year, month, day).lower()
    print(f"{month}-{day}-{year} is a {weekday}.")
dow.makeCalendar()
getDayOfTheWeekForUserDate()
