# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
# Series construction drops any .freq attr
data = data._with_freq(None)
super().test_series_constructor(data)
