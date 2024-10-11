# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
cat = Categorical([1, 2, 3])

# .categories is an index, so we include the hashtable
assert 0 < cat.nbytes <= cat.memory_usage()
assert 0 < cat.nbytes <= cat.memory_usage(deep=True)

cat = Categorical(["foo", "foo", "bar"])
assert cat.memory_usage(deep=True) > cat.nbytes

if not PYPY:
    # sys.getsizeof will call the .memory_usage with
    # deep=True, and add on some GC overhead
    diff = cat.memory_usage(deep=True) - sys.getsizeof(cat)
    assert abs(diff) < 100
