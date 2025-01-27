# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
num_elements = 10
num_epochs = -1
num_outputs = 100
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self,
    lambda: self._build_repeat_dataset(
        num_elements, num_epochs, num_outputs=num_outputs, options=options),
    num_outputs=num_outputs)
