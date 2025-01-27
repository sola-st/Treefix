# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
input_values = np.float32([1., np.nan, 2., np.nan, 3.])
dataset = dataset_ops.Dataset.from_tensor_slices(input_values).map(
    lambda x: array_ops.check_numerics(x, "message")).window(
        size=2, shift=2, stride=2,
        drop_remainder=True).flat_map(lambda x: x.batch(batch_size=2))
self.assertDatasetProduces(
    dataset, expected_output=[np.float32([1., 2.]),
                              np.float32([2., 3.])])
