# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# In particular NumericIndex with dtype float32
index = simple_index
N = len(index)

result = index.append(index)
assert result.dtype == index.dtype
tm.assert_index_equal(result[:N], index, check_exact=True)
tm.assert_index_equal(result[N:], index, check_exact=True)

alt = index.take(list(range(N)) * 2)
tm.assert_index_equal(result, alt, check_exact=True)
