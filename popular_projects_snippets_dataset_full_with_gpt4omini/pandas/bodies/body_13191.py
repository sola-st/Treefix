# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# test additional ExtensionArrays that are supported through the
# __arrow_array__ protocol + by defining a custom ExtensionType
df = pd.DataFrame(
    {
        "c": pd.IntervalIndex.from_tuples([(0, 1), (1, 2), (3, 4)]),
        "d": pd.period_range("2012-01-01", periods=3, freq="D"),
        # GH-45881 issue with interval with datetime64[ns] subtype
        "e": pd.IntervalIndex.from_breaks(
            pd.date_range("2012-01-01", periods=4, freq="D")
        ),
    }
)
check_round_trip(df, pa)
