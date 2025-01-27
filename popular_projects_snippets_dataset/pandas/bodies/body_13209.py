# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
idx = 5 * [timezone_aware_date_list]

df = pd.DataFrame(index=idx, data={"index_as_col": idx})

expected = df.copy()
expected.index.name = "index"
check_round_trip(df, fp, expected=expected)
