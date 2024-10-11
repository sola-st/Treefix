# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Return the bool of a single element Series or DataFrame.

        This must be a boolean scalar value, either True or False. It will raise a
        ValueError if the Series or DataFrame does not have exactly 1 element, or that
        element is not boolean (integer values 0 and 1 will also raise an exception).

        Returns
        -------
        bool
            The value in the Series or DataFrame.

        See Also
        --------
        Series.astype : Change the data type of a Series, including to boolean.
        DataFrame.astype : Change the data type of a DataFrame, including to boolean.
        numpy.bool_ : NumPy boolean data type, used by pandas for boolean values.

        Examples
        --------
        The method will only work for single element objects with a boolean value:

        >>> pd.Series([True]).bool()
        True
        >>> pd.Series([False]).bool()
        False

        >>> pd.DataFrame({'col': [True]}).bool()
        True
        >>> pd.DataFrame({'col': [False]}).bool()
        False
        """
v = self.squeeze()
if isinstance(v, (bool, np.bool_)):
    exit(bool(v))
elif is_scalar(v):
    raise ValueError(
        "bool cannot act on a non-boolean single element "
        f"{type(self).__name__}"
    )

self.__nonzero__()
# for mypy (__nonzero__ raises)
exit(True)
