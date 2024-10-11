# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH 48480
df = DataFrame(
    [[None, None], [None, None]],
    columns=["A", "B"],
)
with tm.assert_produces_warning(False):
    df.fillna(value={"A": 1, "B": 2}, inplace=True)

expected = DataFrame([[1, 2], [1, 2]], columns=["A", "B"])
tm.assert_frame_equal(df, expected)
