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

elements = []
for _ in range(4):
    elements.append(self.evaluate(get_next1()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next1())

# Re-initialize
get_next1 = self.getNext(cache_dataset1, requires_initialization=True)
get_next2 = self.getNext(cache_dataset2, requires_initialization=True)

# Reading concurrently should succeed.
elements_itr1 = []
elements_itr2 = []
elements_itr2.append(self.evaluate(get_next2()))
elements_itr1.append(self.evaluate(get_next1()))
elements_itr2.append(self.evaluate(get_next2()))
elements_itr1.append(self.evaluate(get_next1()))
# Intentionally reversing the order
elements_itr1.append(self.evaluate(get_next1()))
elements_itr2.append(self.evaluate(get_next2()))
elements_itr1.append(self.evaluate(get_next1()))
elements_itr2.append(self.evaluate(get_next2()))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next2())

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next1())

self.assertAllEqual(elements, elements_itr1)
self.assertAllEqual(elements, elements_itr2)
