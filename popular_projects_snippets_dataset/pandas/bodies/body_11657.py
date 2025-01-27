# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
parser = all_parsers
msg = r"but only \d+ lines in file"

with pytest.raises(ValueError, match=msg):
    s = StringIO(",,")
    parser.read_csv(s, header=[10])
