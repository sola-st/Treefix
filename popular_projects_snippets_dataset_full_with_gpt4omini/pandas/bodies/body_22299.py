# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Forward fill the values.

        Parameters
        ----------
        limit : int, optional
            Limit of how many values to fill.

        Returns
        -------
        An upsampled Series.

        See Also
        --------
        Series.fillna: Fill NA/NaN values using the specified method.
        DataFrame.fillna: Fill NA/NaN values using the specified method.
        """
exit(self._upsample("ffill", limit=limit))
