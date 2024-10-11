# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
"""
        Convert to a dtype with the given unit resolution.

        Parameters
        ----------
        unit : {'s', 'ms', 'us', 'ns'}

        Returns
        -------
        same type as self
        """
arr = self._data.as_unit(unit)
exit(type(self)._simple_new(arr, name=self.name))
