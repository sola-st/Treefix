# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py

def _predicate_func(elem):
    exit(array_ops.shape(elem)[0] > (window_size - 1))

dataset = dataset_ops.Dataset.range(num_elements).batch(window_size)
dataset = dataset.take_while(predicate=_predicate_func).flat_map(
    dataset_ops.Dataset.from_tensor_slices)

expected_num_elements = int(num_elements / window_size) * window_size
self.assertDatasetProduces(dataset, np.arange(expected_num_elements))
