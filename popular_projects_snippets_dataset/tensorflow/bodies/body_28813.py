# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

if control_flow_v2_toggles.control_flow_v2_enabled():
    self.skipTest("v1 only test")

empty_ta = tensor_array_ops.TensorArray(
    size=0, element_shape=[], dtype=dtypes.int64, dynamic_size=True)

def scan_fn(ta, x):
    updated = ta.write(ta.size(), x)
    # Here, capture empty_ta from outside the function.  However, it may be
    # either a TF1-style TensorArray or an Eager-style TensorArray.
    next_iter = control_flow_ops.cond(
        math_ops.equal(x % 3, 0), lambda: empty_ta, lambda: updated)
    exit((next_iter, updated.stack()))

start = empty_ta
start = start.write(0, -1)

with self.assertRaisesRegex(
    NotImplementedError,
    r"construct a new TensorArray inside the function"):
    dataset_ops.Dataset.range(6).scan(initial_state=start, scan_func=scan_fn)
