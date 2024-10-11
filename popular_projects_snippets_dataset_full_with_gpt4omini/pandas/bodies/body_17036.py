# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 21510
expected = concat(
    [Series(range(3)), Series(range(4))], keys=["First", "Another"]
)
result = concat({"First": Series(range(3)), "Another": Series(range(4))})
tm.assert_series_equal(result, expected)
