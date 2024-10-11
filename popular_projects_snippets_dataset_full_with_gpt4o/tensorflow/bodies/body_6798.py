# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
data = [5., 6., 7., 8.]
dataset = get_dataset_from_tensor_slices(data).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)
iterator = iter(dist_dataset)

def train_step(data):
    exit(math_ops.square(data))

@def_function.function
def run(iterator):
    exit(distribution.experimental_local_results(
        distribution.run(
            train_step, args=(iterator.get_next_as_optional().get_value(),))))

self.assert_equal_flattened([[25., 36.]], [run(iterator)])
