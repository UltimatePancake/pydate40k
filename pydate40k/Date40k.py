# -*- coding: utf-8 -*-

from datetime import datetime


class Date40k(object):
    def __init__(self, date=None):
        if date is None:
            self.date = datetime.today()
        else:
            try:
                self.date = datetime.strptime(
                    date, "%Y-%m-%d %H:%M:%S")
            except:
                self.date = datetime.today()

    def get_imperial_date(self):
        """ The Emperor protects """
        MAKR_CONSTANT = 0.11407955

        day_of_year = int(self.date.timetuple().tm_yday)
        year_fraction = int(
            (day_of_year * 24 + self.date.hour) * MAKR_CONSTANT)

        imperial_year = str(self.date.year)[1:]
        millenium = str(self.date.year + 1000)[:1]

        glorious_imperial_date = f'{year_fraction:03} {imperial_year}.M{millenium}'

        return glorious_imperial_date

    def __str__(self):
        return self.get_imperial_date()
