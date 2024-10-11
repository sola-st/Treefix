# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
components = list(range(1000))
dataset = dataset_ops.Dataset.from_tensor_slices(components)
shuffled_dataset = dataset.shuffle(buffer_size=1000, seed=124)
shuffled_dataset_2 = dataset.shuffle(buffer_size=1000, seed=51)

shuffled_dataset_array = []
shuffled_dataset_array_2 = []

for i in range(1000):
    shuffled_dataset_array.append(
        self.evaluate(random_access.at(shuffled_dataset, i)))
    shuffled_dataset_array_2.append(
        self.evaluate(random_access.at(shuffled_dataset_2, i)))
self.assertNotEqual(shuffled_dataset_array, shuffled_dataset_array_2)
self.assertAllEqual(
    sorted(shuffled_dataset_array), sorted(shuffled_dataset_array_2))
