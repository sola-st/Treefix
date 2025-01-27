# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 13120
result = klass(memoryview(np.arange(2000, 2005)), **extra_kwargs)
expected = klass(list(range(2000, 2005)), **extra_kwargs)
tm.assert_index_equal(result, expected, exact=True)
