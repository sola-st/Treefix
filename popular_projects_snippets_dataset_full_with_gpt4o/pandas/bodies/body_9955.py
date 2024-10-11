# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH 8080
engine, raw = engine_and_raw
s = Series([None, None, None])
result = s.expanding(min_periods=0).apply(lambda x: len(x), raw=raw, engine=engine)
expected = Series([1.0, 2.0, 3.0])
tm.assert_series_equal(result, expected)
