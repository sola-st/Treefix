# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# GH 4280
# non_unique index with a large selection triggers a memory error

columns = list("ABCDEFG")

df = pd.concat(
    [
        DataFrame(
            np.random.randn(length, len(columns)),
            index=np.arange(length),
            columns=columns,
        ),
        DataFrame(np.ones((l2, len(columns))), index=[0] * l2, columns=columns),
    ]
)

assert df.index.is_unique is False

mask = np.arange(l2)
result = df.loc[mask]
expected = pd.concat(
    [
        df.take([0]),
        DataFrame(
            np.ones((len(mask), len(columns))),
            index=[0] * len(mask),
            columns=columns,
        ),
        df.take(mask[1:]),
    ]
)
tm.assert_frame_equal(result, expected)
