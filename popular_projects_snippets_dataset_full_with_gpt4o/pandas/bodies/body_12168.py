# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
parser = all_parsers
data = "a\n1\n2\n3\n4\n5"
msg = "No columns to parse from file"

with pytest.raises(EmptyDataError, match=msg):
    parser.read_csv(StringIO(data), skiprows=lambda x: True)
