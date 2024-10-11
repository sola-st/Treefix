# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 18455
cols = [1, value, 3]
idx = ["a", value]
values = [[0, 3], [1, 4], [2, 5]]
data = {cols[c]: Series(values[c], index=idx) for c in range(3)}
result = DataFrame(data).sort_values(1).sort_values("a", axis=1)
expected = DataFrame(
    np.arange(6, dtype="int64").reshape(2, 3), index=idx, columns=cols
)
tm.assert_frame_equal(result, expected)

result = DataFrame(data, index=idx).sort_values("a", axis=1)
tm.assert_frame_equal(result, expected)

result = DataFrame(data, index=idx, columns=cols)
tm.assert_frame_equal(result, expected)
