# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH41044
df = DataFrame({"A": ["abc", "def"], "B": ["ghi", "jkl"]}, dtype=dtype)
df.loc[0, :] = {"A": "newA", "B": "newB"}

expected = DataFrame({"A": ["newA", "def"], "B": ["newB", "jkl"]}, dtype=dtype)

tm.assert_frame_equal(df, expected)
