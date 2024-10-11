# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py

# mixed lcd
values = mixed_float_frame[["A", "B", "C", "D"]].values
assert values.dtype == np.float64

values = mixed_float_frame[["A", "B", "C"]].values
assert values.dtype == np.float32

values = mixed_float_frame[["C"]].values
assert values.dtype == np.float16

# GH#10364
# B uint64 forces float because there are other signed int types
values = mixed_int_frame[["A", "B", "C", "D"]].values
assert values.dtype == np.float64

values = mixed_int_frame[["A", "D"]].values
assert values.dtype == np.int64

# B uint64 forces float because there are other signed int types
values = mixed_int_frame[["A", "B", "C"]].values
assert values.dtype == np.float64

# as B and C are both unsigned, no forcing to float is needed
values = mixed_int_frame[["B", "C"]].values
assert values.dtype == np.uint64

values = mixed_int_frame[["A", "C"]].values
assert values.dtype == np.int32

values = mixed_int_frame[["C", "D"]].values
assert values.dtype == np.int64

values = mixed_int_frame[["A"]].values
assert values.dtype == np.int32

values = mixed_int_frame[["C"]].values
assert values.dtype == np.uint8
