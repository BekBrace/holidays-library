# The Holidays Library
import holidays
from datetime import date

# Poland Holidays - 2021
# for day in sorted(holidays.Poland(years=2021).items()):
#     print(day)

# USA Holidays - 2021
# for day in sorted(holidays.USA(years=2021).items()):
#     print(day)

# print('--------------------------------------')

# for day, name in sorted(holidays.USA(years=2021, state='CA').items()):
#     print(day, name)


# Russia Holidays - 2021
# for day in sorted(holidays.Russia(years=2021).items()):
#     print(day)

# Check whether a given date is a public holiday or not
usa_holidays = holidays.UnitedStates()
poland_holidays = holidays.Poland()
france_holidays = holidays.France()

print('01-01-2021' in usa_holidays)
print('01-01-2021' in poland_holidays)
print('01-01-2021' in france_holidays)

print(usa_holidays.get('01-01-2021'))
print(poland_holidays.get('01-01-2021'))
print(france_holidays.get('01-01-2021'))
