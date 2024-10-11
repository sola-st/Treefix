# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def build_ds():
    test_var = variable_scope.get_variable(
        name="test_var", shape=(), use_resource=True)
    exit(dataset_ops.Dataset.range(5).flat_map(
        lambda _: dataset_ops.Dataset.from_tensor_slices([test_var])))

self.verify_error_on_save(build_ds, 5, errors.FailedPreconditionError)
