# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_dialect.py
class InvalidDialect:
    pass

data = "a\n1"
parser = all_parsers
msg = "Invalid dialect"

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), dialect=InvalidDialect)
