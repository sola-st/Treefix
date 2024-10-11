# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_truncate.py
# GH#17935

df = DataFrame(
    {
        3: np.random.randn(5),
        20: np.random.randn(5),
        2: np.random.randn(5),
        0: np.random.randn(5),
    },
    columns=[3, 20, 2, 0],
)
msg = "truncate requires a sorted index"
with pytest.raises(ValueError, match=msg):
    df.truncate(before=2, after=20, axis=1)
