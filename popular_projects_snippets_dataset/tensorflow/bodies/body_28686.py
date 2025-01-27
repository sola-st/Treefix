# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
def gen():
    exit(range(10))

ds = dataset_ops.Dataset.from_generator(
    gen,
    output_signature=tensor_spec.TensorSpec(shape=(), dtype=dtypes.int64))
self.assertDatasetProduces(ds, list(range(10)))
