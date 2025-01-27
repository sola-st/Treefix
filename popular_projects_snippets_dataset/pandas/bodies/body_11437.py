# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
df_result = read_xml(
    xml_dates,
    names=["Col1", "Col2", "Col3", "Col4"],
    dtype={"Col2": "string", "Col3": "Int64", "Col4": "datetime64[ns]"},
    parser=parser,
)
df_iter = read_xml_iterparse(
    xml_dates,
    parser=parser,
    names=["Col1", "Col2", "Col3", "Col4"],
    dtype={"Col2": "string", "Col3": "Int64", "Col4": "datetime64[ns]"},
    iterparse={"row": ["shape", "degrees", "sides", "date"]},
)

df_expected = DataFrame(
    {
        "Col1": ["square", "circle", "triangle"],
        "Col2": Series(["00360", "00360", "00180"]).astype("string"),
        "Col3": Series([4.0, float("nan"), 3.0]).astype("Int64"),
        "Col4": to_datetime(["2020-01-01", "2021-01-01", "2022-01-01"]),
    }
)

tm.assert_frame_equal(df_result, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
