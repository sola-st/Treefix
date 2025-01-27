# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/skip_test.py
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(self, lambda: self._build_skip_dataset(count, options),
          num_outputs)
