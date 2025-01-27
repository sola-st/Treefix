# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
# Equal length elements
elements = [
    np.tile(np.array([[1], [2], [3], [4]]), 20),
    np.tile(np.array([[12], [13], [14], [15]]), 22),
    np.array([37, 38, 39, 40])
]
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self,
    lambda: self._build_list_dataset(elements, options),
    num_outputs=3)
