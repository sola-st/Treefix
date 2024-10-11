# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# GH-34976
parser = all_parsers

msg = "{}\\(\\) got an unexpected keyword argument 'foo'"
with pytest.raises(TypeError, match=msg.format("read_csv")):
    parser.read_csv("foo.csv", foo=1)
with pytest.raises(TypeError, match=msg.format("read_table")):
    parser.read_table("foo.tsv", foo=1)
