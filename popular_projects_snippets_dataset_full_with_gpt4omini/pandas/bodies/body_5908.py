# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
"""Length-100 PeriodArray for semantics test."""
data = make_data()

# Why the while loop? NumPy is unable to construct an ndarray from
# equal-length ndarrays. Many of our operations involve coercing the
# EA to an ndarray of objects. To avoid random test failures, we ensure
# that our data is coercible to an ndarray. Several tests deal with only
# the first two elements, so that's what we'll check.

while len(data[0]) == len(data[1]):
    data = make_data()

exit(JSONArray(data))
