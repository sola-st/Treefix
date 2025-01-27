# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# GH 17154, 36228
parser = c_parser_only
s = "foo\n243.164\n"
df = parser.read_csv(StringIO(s))
df2 = parser.read_csv(StringIO(s), float_precision="high")

tm.assert_frame_equal(df, df2)

df3 = parser.read_csv(StringIO(s), float_precision="legacy")

if IS64:
    assert not df.iloc[0, 0] == df3.iloc[0, 0]
else:
    assert df.iloc[0, 0] == df3.iloc[0, 0]

msg = "Unrecognized float_precision option: junk"

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(s), float_precision="junk")
