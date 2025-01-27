# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
"""
        Analogue to np.putmask(self, mask, value)

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

np.putmask(self._ndarray, mask, value)
