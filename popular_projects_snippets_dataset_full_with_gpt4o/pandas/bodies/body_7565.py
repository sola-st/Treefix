# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py
# test ufuncs of numpy. see:
# https://numpy.org/doc/stable/reference/ufuncs.html

expected_exception = TypeError
msg = (
    "loop of ufunc does not support argument 0 of type tuple which "
    f"has no callable {func.__name__} method"
)
with pytest.raises(expected_exception, match=msg):
    func(idx)
