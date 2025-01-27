# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self, lambda: self._build_dataset(5, 20, options), num_outputs=100)
