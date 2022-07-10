from datetime import datetime, timedelta, date

class Dates:

    def __init__(self, startDate, endDate):
            self.startDate = datetime.strptime(startDate, "%m%d%Y").date()
            self.endDate = datetime.strptime(endDate, "%m%d%Y").date()
            self.interval = 1

    def __init__(self, startDate, endDate, interval):
            self.startDate = datetime.strptime(startDate, "%m%d%Y").date()
            self.endDate = datetime.strptime(endDate, "%m%d%Y").date()
            self.interval = interval

    def getDays(self):
        delta = timedelta(days=self.interval)
        while (self.startDate <= self.endDate):
            print(self.startDate)
            self.startDate += delta

