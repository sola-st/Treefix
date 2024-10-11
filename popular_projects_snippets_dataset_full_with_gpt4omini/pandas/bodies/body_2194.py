# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# 5/25/2012
scalar = np.int64(1337904000000000).view("M8[us]")
as_obj = scalar.astype("O")

index = DatetimeIndex([scalar])
assert index[0] == scalar.astype("O")

value = Timestamp(scalar)
assert value == as_obj
