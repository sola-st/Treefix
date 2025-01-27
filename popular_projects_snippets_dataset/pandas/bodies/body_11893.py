# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
# GH 14135
result = read_fwf(
    StringIO("#\nA1K\n"), colspecs=[(1, 2), (2, 3)], comment="#", header=None
)
expected = DataFrame([[1, "K"]], columns=[0, 1])
tm.assert_frame_equal(result, expected)
