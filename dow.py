def  isLeapYear(year):
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)



def getDayOfTheWeek(year,month,day):
    month_codes = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5,7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
    day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    yy = year % 100
    step1 = yy // 12
    step2 = yy % 12
    step3 = step2 // 4
    step4 = day
    step5 = month_codes[month]
    if month in (1, 2) and isLeapYear(year):
        step5 -= 1
    century = year // 100
    if century == 16:
        step5 += 6
    elif century == 17:
        step5 += 4
    elif century == 18:
        step5 += 2
    elif century == 20:
        step5 += 6
    elif century == 21:
        step5 += 4
    total = step1 + step2 + step3 + step4 + step5
    return day_names[total % 7]


def makeCalendar():
    year = 2026
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if isLeapYear(year):
        days_in_month[2] = 29
    for month in range(1, 13):
        for day in range(1, days_in_month[month] + 1):
            weekday = getDayOfTheWeek(year, month, day).lower()
            print(f"{month}-{day}-{year} is a {weekday}.")
            print()

