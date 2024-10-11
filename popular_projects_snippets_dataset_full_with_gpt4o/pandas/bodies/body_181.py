# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 13820
def apply_list(row):
    exit([2 * row["A"], 2 * row["C"], 2 * row["B"]])

df = DataFrame(np.zeros((4, 4)), columns=list("ABCD"))
result = getattr(df, op)(apply_list, axis=1)
expected = Series(
    [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
)
tm.assert_series_equal(result, expected)
