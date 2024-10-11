# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/zip_test.py
if attr is None:
    self.skipTest("attr module is not available.")

@attr.s
class Foo:
    x = attr.ib()
    y = attr.ib()

x = Foo(x=dataset_ops.Dataset.range(3), y=dataset_ops.Dataset.range(3, 6))
dataset = dataset_ops.Dataset.zip(x)
expected = [Foo(x=0, y=3), Foo(x=1, y=4), Foo(x=2, y=5)]
for i in range(3):
    self.assertAllEqual(
        self.evaluate(random_access.at(dataset, index=i)), expected[i])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(random_access.at(dataset, index=4))
