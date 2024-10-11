# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
dataset = (
    dataset_ops.Dataset.range(10).apply(
        batching.map_and_batch(lambda x: array_ops.reshape(x * x, [1]), 4)))

self.assertEqual(
    [None, 1], dataset_ops.get_legacy_output_shapes(dataset).as_list())
expected_output = [[[0], [1], [4], [9]], [[16], [25], [36], [49]],
                   [[64], [81]]]
self.assertDatasetProduces(dataset, expected_output=expected_output)
