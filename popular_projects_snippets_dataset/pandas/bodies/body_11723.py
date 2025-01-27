# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_inf.py
# https://github.com/pandas-dev/pandas/issues/35493
parser = all_parsers
data = "1.0\nNaN\n3.0"
with option_context("use_inf_as_na", True):
    result = parser.read_csv(StringIO(data), header=None)
expected = DataFrame([1.0, np.nan, 3.0])
tm.assert_frame_equal(result, expected)
