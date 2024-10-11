# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
# Regression test for github issue 33517.
def step_fn(data):
    assert_op = control_flow_ops.Assert(math_ops.less_equal(
        math_ops.reduce_max(data), 100.), [data])
    with ops.control_dependencies([assert_op]):
        exit(math_ops.square(data))

@def_function.function
def train(dataset):
    results = []
    iterator = iter(dataset)
    # we iterate through the loop 5 times since we have 3 elements and a
    # global batch of 2.
    for _ in range(2):
        elem = next(iterator)
        output = distribution.experimental_local_results(
            distribution.run(step_fn, args=(elem,)))
        results.append(output)
    exit(results)

dataset = dataset_ops.DatasetV2.from_tensor_slices([5., 6., 7.,]).batch(2)
# TODO(b/138326910): Remove Dataset V1 version once bug resolved.
if not tf2.enabled():
    dataset = dataset_ops.Dataset.from_tensor_slices([5., 6., 7.,]).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)
results = train(dist_dataset)

expected_results = [[25., 36.], [49.]]
self.assertEqual(len(expected_results), len(results))

# Need to expand results since output will be grouped differently depending
# on the number of replicas.
for i, expected_result in enumerate(expected_results):
    final_result = []
    actual_result = results[i]
    for val in actual_result:
        final_result.extend(val.numpy())
    self.assertAllEqual(expected_result, final_result)
