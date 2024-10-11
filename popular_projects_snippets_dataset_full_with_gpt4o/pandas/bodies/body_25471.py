# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
        Initializes holiday object with a given set a rules.  Normally
        classes just have the rules defined within them.

        Parameters
        ----------
        name : str
            Name of the holiday calendar, defaults to class name
        rules : array of Holiday objects
            A set of rules used to create the holidays.
        """
super().__init__()
if name is None:
    name = type(self).__name__
self.name = name

if rules is not None:
    self.rules = rules
