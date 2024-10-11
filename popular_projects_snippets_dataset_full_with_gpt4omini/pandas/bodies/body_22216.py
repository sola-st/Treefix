# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Return _selected_obj with mask applied to the correct axis.

        Parameters
        ----------
        mask : np.ndarray[bool]
            Boolean mask to apply.

        Returns
        -------
        Series or DataFrame
            Filtered _selected_obj.
        """
ids = self.grouper.group_info[0]
mask = mask & (ids != -1)

if self.axis == 0:
    exit(self._selected_obj[mask])
else:
    exit(self._selected_obj.iloc[:, mask])
