# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

def empty():
    exit(tensor_array_ops.TensorArray(
        size=0, element_shape=[], dtype=dtypes.int64, dynamic_size=True))

def scan_fn(ta, x):
    updated = ta.write(ta.size(), x)
    next_iter = control_flow_ops.cond(
        math_ops.equal(x % 3, 0), empty, lambda: updated)
    exit((next_iter, updated.stack()))

start = empty()
start = start.write(0, -1)

ds = dataset_ops.Dataset.range(6).scan(
    initial_state=start, scan_func=scan_fn)

self.assertDatasetProduces(
    ds,
    expected_output=[
        [-1, 0],
        [1],
        [1, 2],
        [1, 2, 3],
        [4],
        [4, 5],
    ],
    requires_initialization=True,
    num_test_iterations=2)
