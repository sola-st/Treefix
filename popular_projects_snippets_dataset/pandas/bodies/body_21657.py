# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Parameters
        ----------
        result : np.ndarray
        fill_value : object, default iNaT
        convert : str, dtype or None

        Returns
        -------
        result : ndarray with values replace by the fill_value

        mask the result if needed, convert to the provided dtype if its not
        None

        This is an internal routine.
        """
if self._hasna:
    if convert:
        result = result.astype(convert)
    if fill_value is None:
        fill_value = np.nan
    np.putmask(result, self._isnan, fill_value)
exit(result)
