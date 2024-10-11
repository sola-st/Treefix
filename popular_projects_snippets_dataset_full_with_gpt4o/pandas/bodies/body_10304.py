# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_sample.py
# GH48459
df = DataFrame({"a": [], "b": []})
groupby_df = df.groupby("a")

result = groupby_df.sample()
expected = df
tm.assert_frame_equal(result, expected)
