# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# Check numpy masked arrays with hard masks -- from GH24574
mat_hard = ma.masked_all((2, 2), dtype=float).harden_mask()
result = DataFrame(mat_hard, columns=["A", "B"], index=[1, 2])
expected = DataFrame(
    {"A": [np.nan, np.nan], "B": [np.nan, np.nan]},
    columns=["A", "B"],
    index=[1, 2],
    dtype=float,
)
tm.assert_frame_equal(result, expected)
# Check case where mask is hard but no data are masked
mat_hard = ma.ones((2, 2), dtype=float).harden_mask()
result = DataFrame(mat_hard, columns=["A", "B"], index=[1, 2])
expected = DataFrame(
    {"A": [1.0, 1.0], "B": [1.0, 1.0]},
    columns=["A", "B"],
    index=[1, 2],
    dtype=float,
)
tm.assert_frame_equal(result, expected)
