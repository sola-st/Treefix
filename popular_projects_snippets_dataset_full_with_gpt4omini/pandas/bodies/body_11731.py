# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_iterator.py
msg = "'skipfooter' not supported for iteration"
parser = all_parsers
data = "a\n1\n2"

with pytest.raises(ValueError, match=msg):
    with parser.read_csv(StringIO(data), skipfooter=1, **kwargs) as _:
        pass
