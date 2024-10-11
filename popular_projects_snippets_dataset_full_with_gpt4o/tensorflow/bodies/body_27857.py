# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6, 7])
shuffle_dataset = dataset.shuffle(buffer_size=10, seed=2)
batch_dataset = shuffle_dataset.batch(2)

expected_output = [
    np.array([5, 2], dtype=np.int32),
    np.array([4, 7], dtype=np.int32),
    np.array([1, 3], dtype=np.int32),
    np.array([6], dtype=np.int32)
]
for i in range(4):
    self.assertAllEqual(expected_output[i],
                        self.evaluate(random_access.at(batch_dataset, i)))

# Checks the order is consistent with shuffle dataset.
for i in range(3):
    self.assertAllEqual(
        expected_output[i][0],
        self.evaluate(random_access.at(shuffle_dataset, i * 2)))
    self.assertAllEqual(
        expected_output[i][1],
        self.evaluate(random_access.at(shuffle_dataset, (i * 2) + 1)))

# Checks the remainder is the last element in shuffled dataset.
self.assertAllEqual(expected_output[3][0],
                    self.evaluate(random_access.at(shuffle_dataset, 6)))
