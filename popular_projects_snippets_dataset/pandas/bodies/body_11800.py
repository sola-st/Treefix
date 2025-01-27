# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH#41069
parser = all_parsers
data = "a b\n0 1"

sys.setprofile(lambda *a, **k: None)
result = getattr(parser, read_func)(StringIO(data))
sys.setprofile(None)

expected = DataFrame({"a b": ["0 1"]})
tm.assert_frame_equal(result, expected)
