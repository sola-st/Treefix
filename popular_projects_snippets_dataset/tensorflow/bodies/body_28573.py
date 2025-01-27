# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
components = (np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]),
              np.array([9.0, 10.0, 11.0, 12.0]))

def dataset_fn(count=5, filename=None):
    repeat_dataset = (
        dataset_ops.Dataset.from_tensor_slices(components).repeat(count))
    if filename:
        exit(repeat_dataset.cache(filename))
    else:
        exit(repeat_dataset)

self.assertEqual(
    tuple([c.shape[1:] for c in components]),
    dataset_ops.get_legacy_output_shapes(dataset_fn()))

get_next = self.getNext(dataset_fn())

# First run without caching to collect the "ground truth".
elements = []
for _ in range(20):
    elements.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

# Assert that the cached dataset has the same elements as the
# "ground truth".
get_next = self.getNext(dataset_fn(filename=self.cache_prefix))
cached_elements = []
for _ in range(20):
    cached_elements.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertAllEqual(elements, cached_elements)

# Re-initialize with an empty upstream (to throw errors.OutOfRangeError
# if we didn't use the cache).
get_next = self.getNext(dataset_fn(count=0, filename=self.cache_prefix))
replayed_elements = []
for _ in range(20):
    replayed_elements.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertEqual(cached_elements, replayed_elements)

# Re-initialize with an empty upstream and a missing cache file (should
# throw errors.OutOfRangeError immediately).
get_next = self.getNext(
    dataset_fn(count=0, filename=self.cache_prefix + "nonsense"))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
