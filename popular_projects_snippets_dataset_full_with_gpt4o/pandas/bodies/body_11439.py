# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
df_result = read_xml(xml_types, dtype={"degrees": "float"}, parser=parser)
df_iter = read_xml_iterparse(
    xml_types,
    parser=parser,
    dtype={"degrees": "float"},
    iterparse={"row": ["shape", "degrees", "sides"]},
)

df_expected = DataFrame(
    {
        "shape": ["square", "circle", "triangle"],
        "degrees": Series([360, 360, 180]).astype("float"),
        "sides": [4.0, float("nan"), 3.0],
    }
)

tm.assert_frame_equal(df_result, df_expected)
tm.assert_frame_equal(df_iter, df_expected)
