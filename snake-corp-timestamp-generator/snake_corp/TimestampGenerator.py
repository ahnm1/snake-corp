#%%
import calendar
import datetime as dt
from typing import List
from dataclasses import dataclass

@dataclass
class TimestampGenerator:
    for_year: int
    for_month: int

    def get_timestamps(
        self,
        days:list(), 
        minute_increment:int = 15, 
        dt_pattern:str = '%Y%m%d%H%M%S'
    ) -> List[str]:

        monthly_date_range = list()
        for day in range(len(days)):
            daily_date_range = list()
            for hour in range(0,24):
                for minute in range(0,60, minute_increment):
                    daily_date_range.append(
                        dt.datetime(
                            self.for_year,
                            self.for_month,
                            days[day], hour, minute, 0
                        )
                        .strftime(dt_pattern)
                    )
            monthly_date_range.append(daily_date_range)
        return monthly_date_range


    def get_days_for_month(self) -> List[int]:
        days = list()
        for week in calendar.Calendar().yeardayscalendar(self.for_year, 12)[0][self.for_month-1]:
            for day in week:
                if day != 0:
                    days.append(day)
        return [self.for_year, self.for_month, days]


# %%
if __name__ == '__main__':
    from pprint import pprint

    year, month, days = TimestampGenerator(2023,2).get_days_for_month()
    t = TimestampGenerator(year, month).get_timestamps(days)

