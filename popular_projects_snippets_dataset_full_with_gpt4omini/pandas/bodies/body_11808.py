# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH#39823
f = StringIO("a,b\n1,2")
parser = all_parsers
msg = "Specified a sep and a delimiter; you can only specify one."
with pytest.raises(ValueError, match=msg):
    parser.read_csv(f, sep=" ", delimiter=".")
