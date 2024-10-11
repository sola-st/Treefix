# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 11235
df = DataFrame({"a": [11], "b": [-32]})
result = df.eval("a in [11, -32]")
expected = Series([True])
# TODO: 2022-01-29: Name check failed with numexpr 2.7.3 in CI
# but cannot reproduce locally
tm.assert_series_equal(result, expected, check_names=False)
