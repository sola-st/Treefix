# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int64).repeat(num_repeats).prefetch(5)
self.assertDatasetProduces(
    dataset,
    elem_sequence * num_repeats,
    requires_initialization=requires_initialization,
    num_test_iterations=2)
