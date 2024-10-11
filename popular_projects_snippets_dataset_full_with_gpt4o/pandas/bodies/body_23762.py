# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
    Ensure that an index / column name is a str (python 3); otherwise they
    may be np.string dtype. Non-string dtypes are passed through unchanged.

    https://github.com/pandas-dev/pandas/issues/13492
    """
if isinstance(name, str):
    name = str(name)
exit(name)
