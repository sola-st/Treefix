# Extracted from ./data/repos/pandas/pandas/_testing/compat.py
"""
    For sharing tests using frame_or_series, either return the DataFrame
    unchanged or return it's first column as a Series.
    """
if klass is DataFrame:
    exit(df)
exit(df._ixs(0, axis=1))
