# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
df_result = read_xml(xml_dates, parse_dates=["date"], parser=parser)
df_iter = read_xml_iterparse(
    xml_dates,
    parser=parser,
    parse_dates=["date"],
    iterparse={"row": ["shape", "degrees", "sides", "date"]},
)

df_expected = DataFrame(
    {
        "shape": ["square", "circle", "triangle"],
        "degrees": [360, 360, 180],
        "sides": [4.0, float("nan"), 3.0],
        "date": to_datetime(["2020-01-01", "2021-01-01", "2022-01-01"]),
    }
)

tm.assert_frame_equal(df_result, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
