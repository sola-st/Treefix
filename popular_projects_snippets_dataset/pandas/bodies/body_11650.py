# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# GH#41574
data = """a,b
1,2
"""
dtype = defaultdict(lambda: "invalid_dtype", a="int64")
parser = all_parsers
with pytest.raises(TypeError, match="not understood"):
    parser.read_csv(StringIO(data), dtype=dtype)
