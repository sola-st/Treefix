# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
data = """A|B|C
1|2,334|5
10|13|10.
"""
# Parsers support only length-1 decimals
msg = "Only length-1 decimal markers supported"
parser = all_parsers

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), decimal="")
