# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
dataset = get_dataset_from_tensor_slices([5, 6, 7]).batch(4)
mask_dataset = get_dataset_from_tensor_slices([1, 0, 1]).batch(4)
dataset = dataset_ops.DatasetV2.zip((dataset, mask_dataset))

input_iterator = iter(distribution.experimental_distribute_dataset(dataset))
options = distribute_lib.RunOptions(
    experimental_xla_options=tpu.XLAOptions(
        enable_xla_dynamic_padder=False))

@def_function.function
def run(iterator):

    def computation(inputs):
        x, mask = inputs
        y = x * mask
        exit(math_ops.reduce_sum(y))

    inputs = next(iterator)
    outputs = distribution.experimental_local_results(
        distribution.run(computation, args=(inputs,), options=options))
    exit(outputs)

# This assumes that there are exactly 2 replicas
self.assertAllEqual([5, 7], run(input_iterator))
