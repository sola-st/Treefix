# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH 34946
data = """\
    1,2,3
    4,5,6\n"""
parser = all_parsers
with pytest.raises(ValueError, match="Names should be an ordered collection."):
    parser.read_csv(StringIO(data), names=set("QAZ"))
