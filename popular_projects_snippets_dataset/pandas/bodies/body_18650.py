# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH#21866 inconsistent hash-function for float64
# default hash-function would lead to different hash-buckets
# for 0.0 and -0.0 if there are more than 2^30 hash-buckets
# but this would mean 16GB
N = 4  # 12 * 10**8 would trigger the error, if you have enough memory
m = ht.Float64HashTable(N)
m.set_item(0.0, 0)
m.set_item(-0.0, 0)
assert len(m) == 1  # 0.0 and -0.0 are equivalent
