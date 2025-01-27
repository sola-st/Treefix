# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH: 35958
f = StringIO("a  b  c\n1 -2 -3\n4  5   6")
parser = all_parsers
msg = (
    "Specified a delimiter with both sep and "
    "delim_whitespace=True; you can only specify one."
)
with pytest.raises(ValueError, match=msg):
    parser.read_csv(f, delim_whitespace=True, sep=delimiter)

with pytest.raises(ValueError, match=msg):
    parser.read_csv(f, delim_whitespace=True, delimiter=delimiter)
