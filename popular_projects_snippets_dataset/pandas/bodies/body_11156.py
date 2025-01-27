# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
"""
        Run an aggregate func on the subset of data.
        """

def _func(data):
    d = data.loc[data.index.map(lambda x: x.hour < 11)].dropna()
    if fix:
        data[data.index[0]]
    if len(d) == 0:
        exit(None)
    exit(func(d))

exit(_func)
