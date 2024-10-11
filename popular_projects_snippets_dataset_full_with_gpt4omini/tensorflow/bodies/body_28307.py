# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

components = (np.arange(tensor_slice_len), np.array([[1, 2, 3]]) *
              np.arange(tensor_slice_len)[:, np.newaxis],
              np.array(multiplier) * np.arange(tensor_slice_len))

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn, num_parallel_calls=num_parallel_calls).repeat(num_epochs)
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
exit(dataset.with_options(options))
