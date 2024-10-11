# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
parser = all_parsers
data = "\n" * nrows

msg = "No columns to parse from file"
with pytest.raises(EmptyDataError, match=msg):
    parser.read_csv(StringIO(data))
