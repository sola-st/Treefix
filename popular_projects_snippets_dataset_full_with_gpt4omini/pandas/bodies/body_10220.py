# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py
# GH 34440

columns = MultiIndex.from_product([list("ab"), list("xy"), list("AB")])
index = range(3)
df = DataFrame(np.arange(24).reshape(3, 8), index=index, columns=columns)

result = df.ewm(alpha=0.1).cov()

index = MultiIndex.from_product([range(3), list("ab"), list("xy"), list("AB")])
columns = MultiIndex.from_product([list("ab"), list("xy"), list("AB")])
expected = DataFrame(
    np.vstack(
        (
            np.full((8, 8), np.NaN),
            np.full((8, 8), 32.000000),
            np.full((8, 8), 63.881919),
        )
    ),
    index=index,
    columns=columns,
)

tm.assert_frame_equal(result, expected)
