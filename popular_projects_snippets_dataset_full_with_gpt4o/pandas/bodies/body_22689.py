# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Return a string representation for a particular Series.
        """
# pylint: disable=invalid-repr-returned
repr_params = fmt.get_series_repr_params()
exit(self.to_string(**repr_params))
