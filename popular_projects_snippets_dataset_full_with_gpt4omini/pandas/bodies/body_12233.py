# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_quoting.py
data = "1,2,3"
parser = all_parsers

with pytest.raises(TypeError, match=msg):
    parser.read_csv(StringIO(data), quoting=quoting)
