# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
components = (
    np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]),
    np.array([9.0, 10.0, 11.0, 12.0])
)

def dataset_fn(count=5, buffer_size=None, seed=0):
    repeat_dataset = (
        dataset_ops.Dataset.from_tensor_slices(components).repeat(count))
    if buffer_size:
        shuffle_dataset = repeat_dataset.shuffle(buffer_size, seed)

        self.assertEqual(
            tuple([c.shape[1:] for c in components]),
            dataset_ops.get_legacy_output_shapes(shuffle_dataset))
        exit(shuffle_dataset)
    else:
        exit(repeat_dataset)

    # First run without shuffling to collect the "ground truth".
get_next = self.getNext(dataset_fn())
unshuffled_elements = []
for _ in range(20):
    unshuffled_elements.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

# Assert that the shuffled dataset has the same elements as the
# "ground truth".
get_next = self.getNext(dataset_fn(buffer_size=100, seed=37))
shuffled_elements = []
for _ in range(20):
    shuffled_elements.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertAllEqual(sorted(unshuffled_elements), sorted(shuffled_elements))

# Assert that shuffling twice with the same seeds gives the same sequence.
get_next = self.getNext(dataset_fn(buffer_size=100, seed=37))
reshuffled_elements_same_seed = []
for _ in range(20):
    reshuffled_elements_same_seed.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertEqual(shuffled_elements, reshuffled_elements_same_seed)

# Assert that shuffling twice with a different seed gives a different
# permutation of the same elements.
get_next = self.getNext(dataset_fn(buffer_size=100, seed=137))
reshuffled_elements_different_seed = []
for _ in range(20):
    reshuffled_elements_different_seed.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertNotEqual(shuffled_elements, reshuffled_elements_different_seed)
self.assertAllEqual(
    sorted(shuffled_elements), sorted(reshuffled_elements_different_seed))

# Assert that the shuffled dataset has the same elements as the
# "ground truth" when the buffer size is smaller than the input
# dataset.
get_next = self.getNext(dataset_fn(buffer_size=2, seed=37))
reshuffled_elements_small_buffer = []
for _ in range(20):
    reshuffled_elements_small_buffer.append(self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
self.assertAllEqual(
    sorted(unshuffled_elements), sorted(reshuffled_elements_small_buffer))

# Test the case of shuffling an empty dataset.
get_next = self.getNext(dataset_fn(count=0, buffer_size=100, seed=37))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
