# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22295
# create different nans from bit-patterns:
bits_for_nan1 = 0xFFF8000000000001
bits_for_nan2 = 0x7FF8000000000001
NAN1 = struct.unpack("d", struct.pack("=Q", bits_for_nan1))[0]
NAN2 = struct.unpack("d", struct.pack("=Q", bits_for_nan2))[0]
assert NAN1 != NAN1
assert NAN2 != NAN2
a = np.array([NAN1, NAN2], dtype=el_type)
result = pd.unique(a)
assert result.size == 1
# use bit patterns to identify which nan was kept:
result_nan_bits = struct.unpack("=Q", struct.pack("d", result[0]))[0]
assert result_nan_bits == bits_for_nan1
