# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator_with_arg(n):
    for _ in range(n):
        exit(np.array(n, dtype=np.int64))

exit(dataset_ops.Dataset.from_generator(
    generator_with_arg, output_types=dtypes.int64, output_shapes=(),
    args=(elem,)))
