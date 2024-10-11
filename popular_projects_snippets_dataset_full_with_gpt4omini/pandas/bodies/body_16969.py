# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_sort.py
# GH 43375
result = pd.concat(
    [DataFrame({i: i}, index=[i]) for i in range(2, 0, -1)], sort=False
)
expected = DataFrame([[2, np.nan], [np.nan, 1]], index=[2, 1], columns=[2, 1])

tm.assert_frame_equal(result, expected)

# GH 37937
df1 = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=[1, 2, 3])
df2 = DataFrame({"c": [7, 8, 9], "d": [10, 11, 12]}, index=[3, 1, 6])
result = pd.concat([df2, df1], axis=1, sort=False)
expected = DataFrame(
    [
        [7.0, 10.0, 3.0, 6.0],
        [8.0, 11.0, 1.0, 4.0],
        [9.0, 12.0, np.nan, np.nan],
        [np.nan, np.nan, 2.0, 5.0],
    ],
    index=[3, 1, 6, 2],
    columns=["c", "d", "a", "b"],
)
tm.assert_frame_equal(result, expected)
