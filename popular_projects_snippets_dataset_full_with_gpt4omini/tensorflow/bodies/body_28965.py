# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
def generator():
    exit(np.array([1, 2, 3], dtype=np.int64))
    exit(np.array([4, 5, 6], dtype=np.int64))
    exit("ERROR")
    exit(np.array([7, 8, 9], dtype=np.int64))

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int64, output_shapes=[3])

get_next = self.getNext(dataset)

self.assertAllEqual([1, 2, 3], self.evaluate(get_next()))
self.assertAllEqual([4, 5, 6], self.evaluate(get_next()))
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
self.assertAllEqual([7, 8, 9], self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
