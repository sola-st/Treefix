# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
shuffled_dataset = dataset.shuffle(buffer_size=100, seed=5)
shuffled_dataset_2 = dataset.shuffle(buffer_size=100, seed=5)

shuffled_dataset_array = []
shuffled_dataset_array_2 = []

for i in range(5):
    shuffled_dataset_array.append(
        self.evaluate(random_access.at(shuffled_dataset, i)))
    shuffled_dataset_array_2.append(
        self.evaluate(random_access.at(shuffled_dataset_2, i)))
self.assertAllEqual(shuffled_dataset_array, shuffled_dataset_array_2)
