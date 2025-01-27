# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = get_dataset_from_tensor_slices([5., 6., 7.]).batch(4)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

@def_function.function
def run(iterator):
    inputs = next(iterator)
    exit(distribution.reduce(reduce_util.ReduceOp.MEAN, inputs, axis=0))

self.assertAllEqual(6., run(input_iterator))
