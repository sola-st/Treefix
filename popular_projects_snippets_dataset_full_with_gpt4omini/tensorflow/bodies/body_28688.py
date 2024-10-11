# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
data = [(n, n+1) for n in range(10)]

def gen():
    exit(data)

ds = dataset_ops.Dataset.from_generator(
    gen,
    output_signature=(tensor_spec.TensorSpec(shape=(), dtype=dtypes.int64),
                      tensor_spec.TensorSpec(shape=(), dtype=dtypes.int64)))
self.assertDatasetProduces(ds, data)
