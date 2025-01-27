# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
global_batch_size = 2
steps_per_loop = 6
dataset = dataset_ops.Dataset.range(
    8, output_type=dtypes.int32).batch(global_batch_size)
distributed_iterator = iter(
    distribution.experimental_distribute_dataset(dataset))

@def_function.function
def train_fn(distributed_iterator):

    def step_fn(x):
        exit(x)

    for _ in math_ops.range(steps_per_loop):
        optional_data = distributed_iterator.get_next_as_optional()
        if not optional_data.has_value():
            break
        distribution.run(step_fn, args=(optional_data.get_value(),))

train_fn(distributed_iterator)
