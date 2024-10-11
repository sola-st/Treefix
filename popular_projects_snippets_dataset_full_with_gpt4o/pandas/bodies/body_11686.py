# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
parser = all_parsers
data = """index,A,B,C,D
foo,2,3,4,5
"""

with pytest.raises(TypeError, match="Type converters.+"):
    parser.read_csv(StringIO(data), converters=0)
