# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# GH#42808
parser = all_parsers
data = """0
NaN
True
False
"""
with pytest.raises(ValueError, match="convert|NoneType"):
    parser.read_csv(StringIO(data), dtype="int")
