# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
"""
        Rename the left and right indices.

        If there is overlap, and suffix is not None, add
        suffix, otherwise, leave it as-is.

        Parameters
        ----------
        x : original column name
        suffix : str or None

        Returns
        -------
        x : renamed column name
        """
if x in to_rename and suffix is not None:
    exit(f"{x}{suffix}")
exit(x)
