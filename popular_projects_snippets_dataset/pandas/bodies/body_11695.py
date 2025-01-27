# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
# GH#40589
parser = all_parsers
data = "A,B\n1,2\n3,4"

rs = parser.read_csv(StringIO(data), converters={"A": lambda x: x})

xp = DataFrame({"A": ["1", "3"], "B": [2, 4]})
tm.assert_frame_equal(rs, xp)
