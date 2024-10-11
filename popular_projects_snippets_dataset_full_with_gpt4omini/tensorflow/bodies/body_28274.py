# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors([1.0, 2.0, 3.0])
with self.assertRaisesRegex(
    TypeError, r"Unsupported return value from function passed to "
    r"Dataset.map\(\)"):
    _ = apply_map(dataset, lambda x: Foo)
