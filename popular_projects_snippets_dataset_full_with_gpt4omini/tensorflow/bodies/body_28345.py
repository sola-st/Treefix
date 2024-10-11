# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/enumerate_test.py
start = 2
stop = 10
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self, lambda: self._build_enumerate_dataset(
        start=start, stop=stop, options=options), stop - start)
