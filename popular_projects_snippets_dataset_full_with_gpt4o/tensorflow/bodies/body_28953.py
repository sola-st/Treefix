# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
exit((dataset_ops.Dataset.from_generator(
    generator, output_types=(dtypes.int64, dtypes.int64),
    output_shapes=([None], [3]))
        .repeat(num_inner_repeats).prefetch(5)))
