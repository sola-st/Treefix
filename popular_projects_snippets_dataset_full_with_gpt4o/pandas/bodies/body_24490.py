# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Check if parse_dates are in columns.

        If user has provided names for parse_dates, check if those columns
        are available.

        Parameters
        ----------
        columns : list
            List of names of the dataframe.

        Returns
        -------
        The names of the columns which will get parsed later if a dict or list
        is given as specification.

        Raises
        ------
        ValueError
            If column to parse_date is not in dataframe.

        """
cols_needed: Iterable
if is_dict_like(self.parse_dates):
    cols_needed = itertools.chain(*self.parse_dates.values())
elif is_list_like(self.parse_dates):
    # a column in parse_dates could be represented
    # ColReference = Union[int, str]
    # DateGroups = List[ColReference]
    # ParseDates = Union[DateGroups, List[DateGroups],
    #     Dict[ColReference, DateGroups]]
    cols_needed = itertools.chain.from_iterable(
        col if is_list_like(col) and not isinstance(col, tuple) else [col]
        for col in self.parse_dates
    )
else:
    cols_needed = []

cols_needed = list(cols_needed)

# get only columns that are references using names (str), not by index
missing_cols = ", ".join(
    sorted(
        {
            col
            for col in cols_needed
            if isinstance(col, str) and col not in columns
        }
    )
)
if missing_cols:
    raise ValueError(
        f"Missing column provided to 'parse_dates': '{missing_cols}'"
    )
# Convert positions to actual column names
exit([
    col if (isinstance(col, str) or col in columns) else columns[col]
    for col in cols_needed
])
