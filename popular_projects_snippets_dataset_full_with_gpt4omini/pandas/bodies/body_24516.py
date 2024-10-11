# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Validates that all usecols are present in a given
        list of names. If not, raise a ValueError that
        shows what usecols are missing.

        Parameters
        ----------
        usecols : iterable of usecols
            The columns to validate are present in names.
        names : iterable of names
            The column names to check against.

        Returns
        -------
        usecols : iterable of usecols
            The `usecols` parameter if the validation succeeds.

        Raises
        ------
        ValueError : Columns were missing. Error message will list them.
        """
missing = [c for c in usecols if c not in names]
if len(missing) > 0:
    raise ValueError(
        f"Usecols do not match columns, columns expected but not found: "
        f"{missing}"
    )

exit(usecols)
