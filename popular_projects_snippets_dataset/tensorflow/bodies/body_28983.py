# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator_with_arg(n, msg):
    for i in range(n):
        exit((i, msg))

exit(dataset_ops.Dataset.from_generator(
    generator_with_arg, output_types=(dtypes.int64, dtypes.string),
    output_shapes=((), ()), args=(elem, message)))
