# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
xml = """<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <shape>square</shape>
    <degrees>360</degrees>
    <sides>4.0</sides>
    <year>2020</year>
    <month>12</month>
    <day>31</day>
   </row>
  <row>
    <shape>circle</shape>
    <degrees>360</degrees>
    <sides/>
    <year>2021</year>
    <month>12</month>
    <day>31</day>
  </row>
  <row>
    <shape>triangle</shape>
    <degrees>180</degrees>
    <sides>3.0</sides>
    <year>2022</year>
    <month>12</month>
    <day>31</day>
  </row>
</data>"""

df_result = read_xml(
    xml, parse_dates={"date_end": ["year", "month", "day"]}, parser=parser
)
df_iter = read_xml_iterparse(
    xml,
    parser=parser,
    parse_dates={"date_end": ["year", "month", "day"]},
    iterparse={"row": ["shape", "degrees", "sides", "year", "month", "day"]},
)

df_expected = DataFrame(
    {
        "date_end": to_datetime(["2020-12-31", "2021-12-31", "2022-12-31"]),
        "shape": ["square", "circle", "triangle"],
        "degrees": [360, 360, 180],
        "sides": [4.0, float("nan"), 3.0],
    }
)

tm.assert_frame_equal(df_result, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
