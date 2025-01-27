# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    exit(42)

dataset_ops.Dataset.from_generator(
    generator,
    output_types=(dtypes.int64),
    output_shapes=[1],
    name="from_generator")
