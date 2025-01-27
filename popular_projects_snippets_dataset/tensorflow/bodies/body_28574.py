# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
components = (np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]),
              np.array([9.0, 10.0, 11.0, 12.0]))

cache_dataset1 = (
    dataset_ops.Dataset.from_tensor_slices(components).cache(
        self.cache_prefix))
cache_dataset2 = (
    dataset_ops.Dataset.from_tensor_slices(components).cache(
        self.cache_prefix))

get_next1 = self.getNext(cache_dataset1)
get_next2 = self.getNext(cache_dataset2)

self.evaluate(get_next1())  # this should succeed

with self.assertRaises(errors.AlreadyExistsError):
    self.evaluate(get_next2())

self.evaluate(get_next1())  # this should continue to succeed
