from datetime import datetime, timedelta, date

class Dates:
        # Constructor creating self fields to start date, end date
        def __init__(self, startDate, endDate):
                self.startDate = datetime.strptime(startDate, "%y%m%d").date()
                self.endDate = datetime.strptime(endDate, "%y%m%d").date()
                self.interval = 1
                
        # Yields a currunt end trip date to get a price back
        def getDays(self):
                delta = timedelta(days=self.interval)
                while (self.startDate <= self.endDate):
                        yield self.startDate
                        self.startDate += delta

        def startDayGetter(self):
                print(self.startDate.__str__())
                return self.startDate.__str__()
        
        def endDayGetter(self):
                print(self.endDate.__str__())
                return self.endDate.__str__()
        