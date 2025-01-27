# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py

if compression == "snappy":
    pytest.importorskip("snappy")

elif compression == "brotli":
    pytest.importorskip("brotli")

df = pd.DataFrame({"A": [1, 2, 3]})
check_round_trip(df, engine, write_kwargs={"compression": compression})
