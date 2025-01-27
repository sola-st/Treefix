# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 31861
result = DataFrame({"a": ["test"], "b": [np.nan]})
result.loc[:, "b"] = result.loc[:, "b"].astype("Int64")
expected = DataFrame({"a": ["test"], "b": array([NA], dtype="Int64")})
tm.assert_frame_equal(result, expected)
