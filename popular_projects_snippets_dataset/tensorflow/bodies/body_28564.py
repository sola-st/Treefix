# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/concatenate_test.py
num_outputs = 9
array = np.tile(np.array([[16], [17], [18], [19], [20]]), 15)
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(self, lambda: self._build_concatenate_dataset(array, options),
          num_outputs)
