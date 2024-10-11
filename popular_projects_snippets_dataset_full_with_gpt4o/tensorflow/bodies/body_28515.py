# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
shuffled_dataset = dataset.shuffle(buffer_size=100)

dataset_array = []
shuffled_dataset_array = []

for i in range(5):
    shuffled_dataset_array.append(
        self.evaluate(random_access.at(shuffled_dataset, i)))
    dataset_array.append(self.evaluate(random_access.at(dataset, i)))
self.assertAllEqual(sorted(dataset_array), sorted(shuffled_dataset_array))
