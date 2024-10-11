# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 21866
# create different nans from bit-patterns:
NAN1 = struct.unpack("d", struct.pack("=Q", 0x7FF8000000000000))[0]
NAN2 = struct.unpack("d", struct.pack("=Q", 0x7FF8000000000001))[0]
assert NAN1 != NAN1
assert NAN2 != NAN2
a = np.array([NAN1, NAN2])  # NAN1 and NAN2 are equivalent
result = pd.unique(a)
expected = np.array([np.nan])
tm.assert_numpy_array_equal(result, expected)
