# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
def generator():
    exit(1)
    exit([2, 3])

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int64)
self.assertDatasetProduces(dataset, expected_output=[1, [2, 3]])
