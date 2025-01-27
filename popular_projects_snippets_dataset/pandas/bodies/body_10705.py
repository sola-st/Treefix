# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_missing.py

# GH9221
# pass thru keyword arguments to the generated wrapper
# are set if the passed kw is None (only)
df = DataFrame(
    index=pd.MultiIndex.from_product(
        [["value1", "value2"], date_range("2014-01-01", "2014-01-06")]
    ),
    columns=Index(["1", "2"], name="id"),
)
df["1"] = [
    np.nan,
    1,
    np.nan,
    np.nan,
    11,
    np.nan,
    np.nan,
    2,
    np.nan,
    np.nan,
    22,
    np.nan,
]
df["2"] = [
    np.nan,
    3,
    np.nan,
    np.nan,
    33,
    np.nan,
    np.nan,
    4,
    np.nan,
    np.nan,
    44,
    np.nan,
]

expected = df.groupby(level=0, axis=0).fillna(method="ffill")
result = df.T.groupby(level=0, axis=1).fillna(method="ffill").T
tm.assert_frame_equal(result, expected)
