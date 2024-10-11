# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
if engine != "auto":
    pytest.importorskip(engine)
url = (
    "https://raw.githubusercontent.com/pandas-dev/pandas/"
    "main/pandas/tests/io/data/parquet/simple.parquet"
)
df = read_parquet(url)
tm.assert_frame_equal(df, df_compat)
