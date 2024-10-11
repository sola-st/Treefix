# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.range(10).map(
    lambda _: random_ops.random_uniform(()))
with self.assertRaises(errors.FailedPreconditionError):
    self.evaluate(
        dataset._as_serialized_graph(external_state_policy=options_lib
                                     .ExternalStatePolicy.FAIL))
