# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
msg = "engine must be one of 'pyarrow', 'fastparquet'"
with pytest.raises(ValueError, match=msg):
    check_round_trip(df_compat, "foo", "bar")
