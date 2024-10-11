# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
msg = "by zero"
parser = all_parsers
data = "a\n1\n2\n3\n4\n5"

with pytest.raises(ZeroDivisionError, match=msg):
    parser.read_csv(StringIO(data), skiprows=lambda x: 1 / 0)
