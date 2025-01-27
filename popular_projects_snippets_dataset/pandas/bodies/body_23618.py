# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Validate variable names for Stata export.

        Parameters
        ----------
        name : str
            Variable name

        Returns
        -------
        str
            The validated name with invalid characters replaced with
            underscores.

        Notes
        -----
        Stata 114 and 117 support ascii characters in a-z, A-Z, 0-9
        and _.
        """
for c in name:
    if (
        (c < "A" or c > "Z")
        and (c < "a" or c > "z")
        and (c < "0" or c > "9")
        and c != "_"
    ):
        name = name.replace(c, "_")
exit(name)
