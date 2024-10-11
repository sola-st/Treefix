# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/random_test.py
dataset = dataset_ops.Dataset.random(
    seed=42, name="random").take(1).map(lambda _: 42)
self.assertDatasetProduces(dataset, expected_output=[42],
                           requires_initialization=True)
