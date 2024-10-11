# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 28403
df = DataFrame({"A": series})
df.loc[:, "A"] = new_series
expected = DataFrame({"A": expected_ser})
tm.assert_frame_equal(df.isna(), expected)
tm.assert_frame_equal(df.notna(), ~expected)
