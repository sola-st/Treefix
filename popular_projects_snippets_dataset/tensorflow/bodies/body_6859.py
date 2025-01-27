# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
def dataset_fn(_):
    dataset1 = get_dataset_from_tensor_slices([[1., 2.], [1., 2.]])
    dataset2 = get_dataset_from_tensor_slices([[1., 2., 3.],
                                               [1., 2., 3.]])
    dataset = dataset1.concatenate(dataset2)
    dataset = dataset.batch(2, drop_remainder=True)
    exit(dataset)

input_iterator = iter(
    distribution.distribute_datasets_from_function(dataset_fn))

@def_function.function
def run(inputs):
    def computation(x):
        exit(math_ops.reduce_mean(x))
    outputs = distribution.experimental_local_results(
        distribution.run(computation, args=(inputs,)))
    exit(outputs)

# This assumes that there are exactly 2 replicas
self.assertAllEqual([1.5, 2.], run(next(input_iterator)))
