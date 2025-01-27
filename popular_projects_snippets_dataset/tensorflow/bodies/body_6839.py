# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = get_dataset_from_tensor_slices(
    [5]).map(lambda x: math_ops.cast(x, dtypes.int64)).batch(2)
input_iterator = iter(distribution.experimental_distribute_dataset(dataset))

@def_function.function
def run(iterator):

    def computation(x):
        exit(math_ops.add(x, x))

    inputs = next(iterator)
    outputs = distribution.experimental_local_results(
        distribution.run(computation, args=(inputs,)))
    exit(outputs)

# This assumes that there are exactly 2 replicas
result = run(input_iterator)
self.assertAllEqual([10], result[0])
self.assertAllEqual([], result[1])
