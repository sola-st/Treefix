# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
parser = all_parsers
data = """2,0,1
1000,2000,3000
4000,5000,6000"""

result = parser.read_csv(StringIO(data), usecols=usecols)
tm.assert_frame_equal(result, expected)
