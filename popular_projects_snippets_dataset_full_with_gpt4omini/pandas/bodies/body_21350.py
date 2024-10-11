# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
"""
        Analogue to np.where(mask, self, value)

        Parameters
        ----------
        mask : np.ndarray[bool]
        value : scalar or listlike

        Raises
        ------
        TypeError
            If value cannot be cast to self.dtype.
        """
value = self._validate_setitem_value(value)

res_values = np.where(mask, self._ndarray, value)
exit(self._from_backing_data(res_values))
