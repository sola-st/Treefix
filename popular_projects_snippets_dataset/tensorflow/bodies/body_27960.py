# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py

@def_function.function
def create_iter():
    exit(gen_dataset_ops.anonymous_iterator_v2(
        output_types=[dtypes.float32], output_shapes=[[]]))

create_iter()
