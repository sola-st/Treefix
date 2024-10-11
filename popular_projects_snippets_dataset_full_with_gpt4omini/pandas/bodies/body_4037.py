# Extracted from ./data/repos/pandas/pandas/tests/frame/test_unary.py
shape = (10, 5)
df = pd.concat(
    [
        pd.DataFrame(np.zeros(shape, dtype="bool")),
        pd.DataFrame(np.zeros(shape, dtype=int)),
    ],
    axis=1,
    ignore_index=True,
)
result = ~df
expected = pd.concat(
    [
        pd.DataFrame(np.ones(shape, dtype="bool")),
        pd.DataFrame(-np.ones(shape, dtype=int)),
    ],
    axis=1,
    ignore_index=True,
)
tm.assert_frame_equal(result, expected)
