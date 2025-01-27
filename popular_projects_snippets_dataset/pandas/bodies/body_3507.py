# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py

# gh 3016
df = DataFrame(
    [[1.0, 2.0, False, True], [4.0, 5.0, True, False]],
    columns=["A", "B", "bool1", "bool2"],
)

other = DataFrame([[45, 45]], index=[0], columns=["A", "B"])
df.update(other)

expected = DataFrame(
    [[45.0, 45.0, False, True], [4.0, 5.0, True, False]],
    columns=["A", "B", "bool1", "bool2"],
)
tm.assert_frame_equal(df, expected)
