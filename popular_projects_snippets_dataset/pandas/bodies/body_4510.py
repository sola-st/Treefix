# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 14600
s1 = Series([39, 6, 4], index=CategoricalIndex(["female", "male", "unknown"]))
s2 = Series(
    [2, 152, 2, 242, 150],
    index=CategoricalIndex(["f", "female", "m", "male", "unknown"]),
)
result = DataFrame([s1, s2])
expected = DataFrame(
    np.array([[39, 6, 4, np.nan, np.nan], [152.0, 242.0, 150.0, 2.0, 2.0]]),
    columns=["female", "male", "unknown", "f", "m"],
)
tm.assert_frame_equal(result, expected)
