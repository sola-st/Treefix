# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH48480
df = DataFrame(columns=["a", "b"])
expected = df.copy()
rhs = DataFrame(columns=["a"])
with tm.assert_produces_warning(None):
    df.loc[:, "a"] = rhs
tm.assert_frame_equal(df, expected)
