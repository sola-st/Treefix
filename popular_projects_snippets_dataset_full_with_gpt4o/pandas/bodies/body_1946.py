# Extracted from ./data/repos/pandas/pandas/tests/api/test_api.py
# see which names are in the namespace, minus optional
# ignored ones
# compare vs the expected

result = sorted(
    f for f in dir(namespace) if not f.startswith("__") and f != "annotations"
)
if ignored is not None:
    result = sorted(set(result) - set(ignored))

expected = sorted(expected)
tm.assert_almost_equal(result, expected)
