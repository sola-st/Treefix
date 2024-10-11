# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
parser = all_parsers
data = """A,B,C,D
a,1,2,01/01/2009
b,3,4,01/02/2009
c,4,5,01/03/2009
"""
result = parser.read_csv(StringIO(data), converters={column: converter})

expected = parser.read_csv(StringIO(data))
expected["D"] = expected["D"].map(converter)

tm.assert_frame_equal(result, expected)
