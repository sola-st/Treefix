# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
target_dist = np.array([0.5, 0.5], dtype=target_dtype)

if init_dtype is None:
    init_dist = None
else:
    init_dist = np.array([0.5, 0.5], dtype=init_dtype)

dataset = dataset_ops.Dataset.range(10)
dataset = dataset.rejection_resample(
    class_func=lambda x: x % 2,
    target_dist=target_dist,
    initial_dist=init_dist)
get_next = self.getNext(dataset, requires_initialization=True)
self.evaluate(get_next())
