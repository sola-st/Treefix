# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
exit(dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int64, output_shapes=[]).prefetch(2))
