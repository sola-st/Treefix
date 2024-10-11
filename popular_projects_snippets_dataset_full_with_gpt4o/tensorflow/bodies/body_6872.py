# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def step_fn(data):
    exit(math_ops.square(data))

@def_function.function
def train(dataset):
    results = []
    iterator = iter(dataset)
    # we iterate through the loop 2 times since we have 4 elements and a
    # global batch of 2.
    for _ in range(2):
        elem = next(iterator)
        output = distribution.experimental_local_results(
            distribution.run(step_fn, args=(elem,)))
        results.append(output)
    exit(results)

dataset = get_dataset_from_tensor_slices([5., 6., 7., 8.]).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)
results = train(dist_dataset)
self.assert_equal_flattened([[25., 36.], [49., 64.]], results)
