# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
div = 3
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
num_outputs = sum(x % 3 != 2 for x in range(100))
verify_fn(self, lambda: self._build_filter_range_dataset(div, options),
          num_outputs)
