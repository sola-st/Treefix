# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
num_elements = 0
num_epochs = -1
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self,
    lambda: self._build_repeat_dataset(
        num_elements, num_epochs, options=options),
    num_outputs=0)
