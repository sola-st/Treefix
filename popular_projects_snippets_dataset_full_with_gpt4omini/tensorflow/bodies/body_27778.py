# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
dataset = dataset_ops.Dataset.range(100)
dataset = dataset.window(30, drop_remainder=True)
dataset = dataset.flat_map(lambda x: x.batch(30))
dataset = dataset.batch(4)

self.assertDatasetProduces(
    dataset,
    expected_output=[[[y + 30 * x for y in range(30)] for x in range(3)]])
