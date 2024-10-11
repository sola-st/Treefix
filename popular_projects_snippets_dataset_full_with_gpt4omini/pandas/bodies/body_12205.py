# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# GH#46997
parser = all_parsers
usecols = lambda header: header.strip() in ["0", "1"]
result = parser.read_csv(StringIO("0,1\nx,y,z"), index_col=False, usecols=usecols)
expected = DataFrame({"0": ["x"], "1": "y"})
tm.assert_frame_equal(result, expected)
