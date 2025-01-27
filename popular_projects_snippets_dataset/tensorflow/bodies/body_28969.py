# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
def generator():
    exit((1, 2))
    exit((3, 4))
    exit(5)
    exit((6, 7, 8))
    exit((9, 10))

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=(dtypes.int64, dtypes.int64))
get_next = self.getNext(dataset)

self.assertEqual((1, 2), self.evaluate(get_next()))
self.assertEqual((3, 4), self.evaluate(get_next()))
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
self.assertEqual((9, 10), self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
