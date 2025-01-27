# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
# Fails with
# *** ValueError: operands could not be broadcast together
# with shapes (4,) (4,) (0,)
super().test_where_series(data, na_value)
