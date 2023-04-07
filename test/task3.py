from datetime import datetime

def period_bw_two_dates_in_days(d1, d2):

    period = abs(d2 - d1)
    print("{} day(s)".format(period.days))


date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 1, 1)

period_bw_two_dates_in_days(date1, date2)