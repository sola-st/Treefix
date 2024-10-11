# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
values = [1, 2, 3, 4, 5, 6]
values_as_array = np.asarray(values)

# Tensor dataset
dataset = tf.data.Dataset.from_tensors(values_as_array)

for value, value_from_dataset in zip([values_as_array], dataset):
    self.assertIsInstance(value_from_dataset, np.ndarray)
    self.assertAllEqual(value_from_dataset, value)

# Tensor slice dataset
dataset = tf.data.Dataset.from_tensor_slices(values_as_array)

for value, value_from_dataset in zip(values, dataset):
    self.assertIsInstance(value_from_dataset, np.ndarray)
    self.assertAllEqual(value_from_dataset, value)

# # TODO(nareshmodi): as_numpy_iterator() doesn't work.
# items = list(dataset.as_numpy_iterator())

# Map over a dataset.
dataset = dataset.map(lambda x: np.add(x, 1))

for value, value_from_dataset in zip(values, dataset):
    self.assertIsInstance(value_from_dataset, np.ndarray)
    self.assertAllEqual(value_from_dataset, value + 1)

# Batch a dataset.
dataset = tf.data.Dataset.from_tensor_slices(values_as_array).batch(2)

for value, value_from_dataset in zip([[1, 2], [3, 4], [5, 6]], dataset):
    self.assertIsInstance(value_from_dataset, np.ndarray)
    self.assertAllEqual(value_from_dataset, value)
