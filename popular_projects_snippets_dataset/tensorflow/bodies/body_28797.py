# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/counter_test.py
num_outputs = 10
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self, lambda: self._build_counter_dataset(
        start=2, step=10, num_outputs=num_outputs, options=options),
    num_outputs)
