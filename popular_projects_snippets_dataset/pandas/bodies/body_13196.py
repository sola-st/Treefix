# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
import pyarrow

df = df_full

# additional supported types for pyarrow
dti = pd.date_range("20130101", periods=3, tz="Europe/Brussels")
dti = dti._with_freq(None)  # freq doesn't round-trip
df["datetime_tz"] = dti
df["bool_with_none"] = [True, None, True]

pa_table = pyarrow.Table.from_pandas(df)
expected = pd.DataFrame(
    {
        col_name: pd.arrays.ArrowExtensionArray(pa_column)
        for col_name, pa_column in zip(
            pa_table.column_names, pa_table.itercolumns()
        )
    }
)
# pyarrow infers datetimes as us instead of ns
expected["datetime"] = expected["datetime"].astype("timestamp[us][pyarrow]")
expected["datetime_with_nat"] = expected["datetime_with_nat"].astype(
    "timestamp[us][pyarrow]"
)
expected["datetime_tz"] = expected["datetime_tz"].astype(
    pd.ArrowDtype(pyarrow.timestamp(unit="us", tz="Europe/Brussels"))
)

with pd.option_context("mode.dtype_backend", "pyarrow"):
    check_round_trip(
        df,
        engine=pa,
        read_kwargs={"use_nullable_dtypes": True},
        expected=expected,
    )
