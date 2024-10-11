# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
def gen():
    exit(42)

dataset = dataset_ops.Dataset.from_generator(gen, dtypes.int32)
self._testNumInputs(dataset, 1)
