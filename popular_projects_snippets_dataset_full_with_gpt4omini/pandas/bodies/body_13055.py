# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH 30986
midx = MultiIndex.from_arrays(
    [
        range(4),
        pd.interval_range(
            start=pd.Timestamp("2020-01-01"), periods=4, freq="6M"
        ),
    ]
)
df = DataFrame(range(4), index=midx)
with tm.ensure_clean(ext) as pth:
    df.to_excel(pth)
    result = pd.read_excel(pth, index_col=[0, 1])
expected = DataFrame(
    range(4),
    MultiIndex.from_arrays(
        [
            range(4),
            [
                "(2020-01-31, 2020-07-31]",
                "(2020-07-31, 2021-01-31]",
                "(2021-01-31, 2021-07-31]",
                "(2021-07-31, 2022-01-31]",
            ],
        ]
    ),
)
tm.assert_frame_equal(result, expected)
