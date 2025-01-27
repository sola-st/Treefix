# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
a = dataset_ops.Dataset.from_tensor_slices([1., 2., 0., 4.])
b = a.map(lambda x: array_ops.check_numerics(1. / x, "error"))

dataset = dataset_ops.Dataset.zip((b, a)).ignore_errors()
get_next = self.getNext(dataset)

for x in [1., 2., 4.]:
    self.assertEqual((1. / x, x), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
