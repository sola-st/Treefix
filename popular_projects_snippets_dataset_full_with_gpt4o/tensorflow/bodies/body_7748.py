# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

@def_function.function
def create_iter():
    with ops.device("/device:TPU:0"):
        exit(gen_dataset_ops.anonymous_iterator_v3(
            output_types=[dtypes.float32], output_shapes=[[]]))

create_iter()
