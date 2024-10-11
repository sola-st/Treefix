# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
        Merge holiday calendars together.  The caller's class
        rules take precedence.  The merge will be done
        based on each holiday's name.

        Parameters
        ----------
        other : holiday calendar
        inplace : bool (default=False)
            If True set rule_table to holidays, else return array of Holidays
        """
holidays = self.merge_class(self, other)
if inplace:
    self.rules = holidays
else:
    exit(holidays)
