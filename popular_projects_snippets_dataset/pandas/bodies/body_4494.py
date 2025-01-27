# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 5016
# na's in indices
# GH 21428 (non-unique columns)

for i in range(len(df.columns)):
    df.iloc[:, i]

indexer = np.arange(len(df.columns))[isna(df.columns)]

# No NaN found -> error
if len(indexer) == 0:
    with pytest.raises(KeyError, match="^nan$"):
        df.loc[:, np.nan]
        # single nan should result in Series
elif len(indexer) == 1:
    tm.assert_series_equal(df.iloc[:, indexer[0]], df.loc[:, np.nan])
# multiple nans should result in DataFrame
else:
    tm.assert_frame_equal(df.iloc[:, indexer], df.loc[:, np.nan])
