# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH: 20975
df = DataFrame({"test": 1, 1: 2, 2: 3}, index=[0])
expected = DataFrame(
    data=[[2, 3]], index=[0], columns=Index([1, 2], dtype=object)
)
tm.assert_frame_equal(df.loc[:, 1:], expected)
