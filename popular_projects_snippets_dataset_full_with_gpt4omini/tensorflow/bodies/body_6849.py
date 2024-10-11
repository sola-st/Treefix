# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = get_dataset_from_tensor_slices([5., 6., 7.]).batch(4)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

@def_function.function
def run(inputs):
    def computation(x):
        exit(array_ops.size_v2(x))
    outputs = distribution.experimental_local_results(
        distribution.run(computation, args=(inputs,)))
    exit(outputs)

# This assumes that there are exactly 2 replicas
self.assertAllEqual([2, 1], run(next(input_iterator)))
