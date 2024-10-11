# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# use the set option

with pd.option_context("io.parquet.engine", "pyarrow"):
    check_round_trip(df_compat)
