# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
dataset = dataset_ops.Dataset.range(10)

def stateful_scan(state, element):
    exit((state, self._statefulBoolFunc(element)))

dataset = dataset.apply(scan_ops.scan(0, stateful_scan))
self._assertNotCheckpointable(dataset)
