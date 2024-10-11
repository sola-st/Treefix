# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

def scan_fn(ta, x):
    exit((ta.write(ta.size(), x), ta.stack()))

start = tensor_array_ops.TensorArray(
    size=0, element_shape=[], dtype=dtypes.int64, dynamic_size=True)
start = start.write(0, -1)

ds = dataset_ops.Dataset.range(5).scan(
    initial_state=start, scan_func=scan_fn)

self.assertDatasetProduces(
    ds,
    expected_output=[
        [-1],
        [-1, 0],
        [-1, 0, 1],
        [-1, 0, 1, 2],
        [-1, 0, 1, 2, 3],
    ],
    requires_initialization=True,
    num_test_iterations=2)
