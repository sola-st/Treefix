# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-6607
data = "a b c\n1 2 3"
parser = all_parsers

with pytest.raises(ValueError, match="you can only specify one"):
    parser.read_csv(StringIO(data), sep=r"\s", delim_whitespace=True)
