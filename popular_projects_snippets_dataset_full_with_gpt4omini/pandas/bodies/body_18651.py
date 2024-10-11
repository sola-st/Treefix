# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH#21866 inconsistent hash-function for float64
# create different nans from bit-patterns:
NAN1 = struct.unpack("d", struct.pack("=Q", 0x7FF8000000000000))[0]
NAN2 = struct.unpack("d", struct.pack("=Q", 0x7FF8000000000001))[0]
assert NAN1 != NAN1
assert NAN2 != NAN2
# default hash function would lead to different hash-buckets
# for NAN1 and NAN2 even if there are only 4 buckets:
m = ht.Float64HashTable()
m.set_item(NAN1, 0)
m.set_item(NAN2, 0)
assert len(m) == 1  # NAN1 and NAN2 are equivalent
