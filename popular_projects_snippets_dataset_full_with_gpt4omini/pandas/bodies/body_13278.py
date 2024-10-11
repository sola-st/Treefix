# Extracted from ./data/repos/pandas/pandas/tests/io/test_gcs.py
"""
    Test that many to/read functions support GCS.

    GH 33987
    """

df1 = DataFrame(
    {
        "int": [1, 3],
        "float": [2.0, np.nan],
        "str": ["t", "s"],
        "dt": date_range("2018-06-18", periods=2),
    }
)

path = f"gs://test/test.{format}"

if format == "csv":
    df1.to_csv(path, index=True)
    df2 = read_csv(path, parse_dates=["dt"], index_col=0)
elif format == "excel":
    path = "gs://test/test.xlsx"
    df1.to_excel(path)
    df2 = read_excel(path, parse_dates=["dt"], index_col=0)
elif format == "json":
    df1.to_json(path)
    df2 = read_json(path, convert_dates=["dt"])
elif format == "parquet":
    pytest.importorskip("pyarrow")
    df1.to_parquet(path)
    df2 = read_parquet(path)
elif format == "markdown":
    pytest.importorskip("tabulate")
    df1.to_markdown(path)
    df2 = df1

tm.assert_frame_equal(df1, df2)
