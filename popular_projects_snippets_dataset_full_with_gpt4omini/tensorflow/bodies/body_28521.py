# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
dataset = dataset_ops.Dataset.range(10).map(
    lambda x: {"foo": x * 2, "bar": x ** 2}).flat_map(
        lambda d: dataset_ops.Dataset.from_tensors(
            d["foo"]).repeat(d["bar"]))
get_next = self.getNext(dataset)
for i in range(10):
    for _ in range(i**2):
        self.assertEqual(i * 2, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
