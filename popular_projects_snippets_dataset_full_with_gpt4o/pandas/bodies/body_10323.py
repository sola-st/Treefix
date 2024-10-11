# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# https://github.com/pandas-dev/pandas/issues/32800
# None should be preserved as object dtype
df = DataFrame.from_dict({"id": ["a"], "value": [None]})
groups = df.groupby("id", as_index=False)
result = getattr(groups, method)()

tm.assert_frame_equal(result, df)
