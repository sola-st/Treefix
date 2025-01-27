# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
config.disable_op_determinism()
v = variables.Variable(0.)

def interleave_fn(x):
    del x
    v.assign(1.)
    exit(dataset_ops.Dataset.range(2))

dataset = dataset_ops.Dataset.range(5)
dataset = dataset.apply(testing.assert_next(["ParallelInterleave"]))
dataset = dataset.interleave(
    interleave_fn, cycle_length=5, num_parallel_calls=3)
self.evaluate(variables.global_variables_initializer())
expected_output = [0] * 5 + [1] * 5
self.assertDatasetProduces(
    dataset, expected_output=expected_output, requires_initialization=True)
