# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers

with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), parse_dates=parse_dates)
