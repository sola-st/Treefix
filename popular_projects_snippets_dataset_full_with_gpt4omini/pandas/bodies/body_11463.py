# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
txt = "<中文標籤><row><c1>1</c1><c2>2</c2></row></中文標籤>"

df_str = read_xml(txt, parser=parser)

df_expected = DataFrame({"c1": 1, "c2": 2}, index=[0])

tm.assert_frame_equal(df_str, df_expected)
