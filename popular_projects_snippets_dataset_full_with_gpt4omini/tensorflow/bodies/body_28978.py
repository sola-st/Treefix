# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# Use an `Event` to signal that the generator has been deleted.
event = threading.Event()

class GeneratorWrapper:

    def __iter__(self):
        exit(self)

    def next(self):
        exit(self.__next__())

    def __next__(self):
        exit(42)

    def __del__(self):
        event.set()

dataset = dataset_ops.Dataset.from_generator(
    GeneratorWrapper, output_types=dtypes.int64).take(2)
get_next = self.getNext(dataset)

self.assertAllEqual(42, self.evaluate(get_next()))
self.assertAllEqual(42, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
# Test that `GeneratorWrapper` object is destroyed when the
# iterator terminates (and the generator iterator is deleted).
self.assertTrue(event.is_set())
