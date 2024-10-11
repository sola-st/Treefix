# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
df_result = read_xml(xml_types, dtype={"sides": "Int64"}, parser=parser)
df_iter = read_xml_iterparse(
    xml_types,
    parser=parser,
    dtype={"sides": "Int64"},
    iterparse={"row": ["shape", "degrees", "sides"]},
)

df_expected = DataFrame(
    {
        "shape": ["square", "circle", "triangle"],
        "degrees": [360, 360, 180],
        "sides": Series([4.0, float("nan"), 3.0]).astype("Int64"),
    }
)

tm.assert_frame_equal(df_result, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
