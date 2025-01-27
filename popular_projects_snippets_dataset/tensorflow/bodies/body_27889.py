# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
arr = np.array(1)
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self, lambda: self._build_tensor_dataset(arr, options), num_outputs=1)
