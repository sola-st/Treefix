# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH#48944
df = pd.DataFrame(data={"A": [0, 1], "B": [1, 0]})
with tm.ensure_clean("test.parquet") as path:
    with open(path.encode(), "wb") as f:
        df.to_parquet(f)

    result = read_parquet(path, engine=engine)
tm.assert_frame_equal(result, df)
