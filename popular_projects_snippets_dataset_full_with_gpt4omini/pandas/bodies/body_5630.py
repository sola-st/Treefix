# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 21866
# create different nans from bit-patterns,
# these nans will land in different buckets in the hash-table
# if no special care is taken
NAN1 = struct.unpack("d", struct.pack("=Q", 0x7FF8000000000000))[0]
NAN2 = struct.unpack("d", struct.pack("=Q", 0x7FF8000000000001))[0]
assert NAN1 != NAN1
assert NAN2 != NAN2

# check that NAN1 and NAN2 are equivalent:
arr = np.array([NAN1, NAN2], dtype=np.float64)
lookup1 = np.array([NAN1], dtype=np.float64)
result = algos.isin(arr, lookup1)
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)

lookup2 = np.array([NAN2], dtype=np.float64)
result = algos.isin(arr, lookup2)
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
