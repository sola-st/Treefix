# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def dataset_fn(_):
    data = array_ops.zeros(5, dtype=dtypes.int32)
    dataset = get_dataset_from_tensor_slices(data)
    dataset = dataset.batch(3)
    exit(dataset)

input_iterator = iter(
    distribution.distribute_datasets_from_function(dataset_fn))

@def_function.function
def step_fn(example):
    segment_ids = array_ops.zeros_like_v2(example)
    num_segment = array_ops.shape(example)[0]
    # If number of segments is dynamic, output should be a dynamic shape.
    exit(math_ops.unsorted_segment_sum(example, segment_ids, num_segment))

# This assumes that there are exactly 2 replicas
outputs = distribution.experimental_local_results(
    distribution.run(step_fn, args=(next(input_iterator),)))
self.assertAllEqual((3,), outputs[0].shape)
self.assertAllEqual((2,), outputs[1].shape)
