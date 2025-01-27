# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
# Equal length components
components = (np.tile(np.array([[1], [2], [3], [4]]),
                      20), np.tile(np.array([[12], [13], [14], [15]]),
                                   22), np.array([37.0, 38.0, 39.0, 40.0]))
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self,
    lambda: self._build_tensor_slices_dataset(components, options),
    num_outputs=4)
