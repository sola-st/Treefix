# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# Provide a different name for each Series.  In this case, groupby
# should not attempt to propagate the Series name since they are
# inconsistent.
exit(Series({"count": 1, "mean": 2, "omissions": 3}, name=df.iloc[0]["A"]))
