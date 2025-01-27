# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH31517
df = DataFrame({"grp": [1, 2, 3, 4, 5]}, dtype="Int64")
result = df.replace(1, 10)
expected = DataFrame({"grp": [10, 2, 3, 4, 5]}, dtype="Int64")
tm.assert_frame_equal(result, expected)
