# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
import pyarrow

df = pd.DataFrame({"x": [0, 1]})
schema = pyarrow.schema([pyarrow.field("x", type=pyarrow.bool_())])
out_df = df.astype(bool)
check_round_trip(df, pa, write_kwargs={"schema": schema}, expected=out_df)
