# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
series_result = getattr(series.ewm(com=10), name)()
assert isinstance(series_result, Series)
