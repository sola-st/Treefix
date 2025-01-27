# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ignore_errors_test.py
components = np.array([1., 2., 3., np.nan, 5.]).astype(np.float32)

dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = dataset.map(lambda x: array_ops.check_numerics(x, "message"))
dataset = dataset.ignore_errors()
options = options_lib.Options()
options.experimental_external_state_policy = (
    options_lib.ExternalStatePolicy.IGNORE)
exit(dataset.with_options(options))
