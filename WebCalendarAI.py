import calendar
import time
from datetime import datetime
class WebCalendarAI:
    avilableDays = None

    def getCurrentMonths(self):
        months = []
        for i in range(0, 13): 
            months.append(calendar.month_name[i])

        return months[int(datetime.today().month)]

    def getCurrentDays(self):
        days = []
        cal = calendar.Calendar()
        for x in cal.itermonthdays(2019, int(datetime.today().month)):
            #if x > 0:
            days.append(x)

        return days

    def MakeWorkOut(self, gender, age, avilableDays):
        #Need more webpages.
        x=4

