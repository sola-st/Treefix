# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
df = DataFrame(
    [[1.5, np.nan, 3.0], [1.5, np.nan, 3.0], [1.5, np.nan, 3], [1.5, np.nan, 3]]
)

other = DataFrame([[3.6, 2.0, np.nan], [np.nan, np.nan, 7]], index=[1, 3])

df.update(other)

expected = DataFrame(
    [[1.5, np.nan, 3], [3.6, 2, 3], [1.5, np.nan, 3], [1.5, np.nan, 7.0]]
)
tm.assert_frame_equal(df, expected)
