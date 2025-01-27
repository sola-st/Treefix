# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
parser = all_parsers
data = "+++123456789...\ncol1,col2,col3,col4\n1,2,3,4\n"
msg = "Expected 2 fields in line 2, saw 4"
if parser.engine == "c":
    msg = (
        "Could not construct index. Requested to use 1 "
        "number of columns, but 3 left to parse."
    )

with pytest.raises(ParserError, match=msg):
    parser.read_csv(StringIO(data), index_col=0, on_bad_lines="error")
