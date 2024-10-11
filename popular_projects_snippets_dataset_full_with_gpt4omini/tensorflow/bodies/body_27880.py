# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
Foo = collections.namedtuple("Foo", ["x", "y"])
element = Foo(x=1, y=2)
dataset = dataset_ops.Dataset.from_tensors(element)
self.assertDatasetProduces(dataset, expected_output=[element])
