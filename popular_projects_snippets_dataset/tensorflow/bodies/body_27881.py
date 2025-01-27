# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
if attr is None:
    self.skipTest("attr module is not available.")

@attr.s
class Foo:
    x = attr.ib()
    y = attr.ib()

element = Foo(x=1, y=2)
dataset = dataset_ops.Dataset.from_tensors(element)
self.assertDatasetProduces(dataset, expected_output=[element])
