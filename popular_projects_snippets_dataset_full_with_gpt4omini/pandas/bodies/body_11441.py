# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml_dtypes.py
df_expected = DataFrame(
    {
        "shape": ["square", "circle", "triangle"],
        "degrees": ["00360", "00360", "00180"],
        "sides": [4.0, float("nan"), 3.0],
    }
)

with tm.assert_produces_warning(ParserWarning, match="Both a converter and dtype"):
    df_result = read_xml(
        xml_types,
        dtype={"degrees": "str"},
        converters={"degrees": str},
        parser=parser,
    )
    df_iter = read_xml_iterparse(
        xml_types,
        dtype={"degrees": "str"},
        converters={"degrees": str},
        parser=parser,
        iterparse={"row": ["shape", "degrees", "sides"]},
    )

    tm.assert_frame_equal(df_result, df_expected)
    tm.assert_frame_equal(df_iter, df_expected)
