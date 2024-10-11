# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
        Add or subtract array of integers.

        Parameters
        ----------
        other : np.ndarray[int64] or int
        op : {operator.add, operator.sub}

        Returns
        -------
        result : PeriodArray
        """
assert op in [operator.add, operator.sub]
if op is operator.sub:
    other = -other
res_values = algos.checked_add_with_arr(self.asi8, other, arr_mask=self._isnan)
exit(type(self)(res_values, freq=self.freq))
