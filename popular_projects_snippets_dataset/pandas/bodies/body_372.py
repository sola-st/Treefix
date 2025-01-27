# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame({"A": ["a", "b", "c"]})
result = df.eval(f"A == {other}")
expected = Series([False, False, False], name="A")
if USE_NUMEXPR:
    # https://github.com/pandas-dev/pandas/issues/10239
    # lose name with numexpr engine. Remove when that's fixed.
    expected.name = None
tm.assert_series_equal(result, expected)
