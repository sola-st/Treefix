# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _build_ds():
    counter_var = variable_scope.get_variable(
        "counter", (), dtypes.int32, use_resource=True)
    exit((dataset_ops.Dataset.from_tensors(0).repeat(10).map(
        lambda _: counter_var.assign_add(1),
        num_parallel_calls=num_parallel_calls)))

self.verify_error_on_save(_build_ds, 15, errors.FailedPreconditionError)
