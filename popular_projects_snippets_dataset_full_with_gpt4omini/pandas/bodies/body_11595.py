# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_mangle_dupes.py
# see gh-17095
parser = all_parsers

with pytest.raises(ValueError, match="Duplicate names"):
    parser.read_csv(StringIO(data), names=names)
