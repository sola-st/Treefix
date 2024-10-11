# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# see gh-5636
parser = all_parsers
msg = (
    "Only booleans, lists, and dictionaries "
    "are accepted for the 'parse_dates' parameter"
)
data = """A,B,C
    1,2,2003-11-1"""

with pytest.raises(TypeError, match=msg):
    parser.read_csv(StringIO(data), parse_dates="C", **kwargs)
