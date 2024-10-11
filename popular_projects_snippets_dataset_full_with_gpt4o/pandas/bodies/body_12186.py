# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# see gh-20558
parser = all_parsers
data = """foo, bar, baz
1000, 2000, 3000
4000, 5000, 6000"""

with pytest.raises(ValueError, match=_msg_validate_usecols_arg):
    parser.read_csv(StringIO(data), usecols="foo")
