# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# see gh-9798
data = "a,b\n1,2"
parser = all_parsers

msg = "The value of index_col couldn't be 'True'"
with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), index_col=True)
