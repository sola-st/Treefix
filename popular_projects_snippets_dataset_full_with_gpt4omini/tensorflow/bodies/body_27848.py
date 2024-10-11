# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
tensor_slice_len = 8
batch_size = 2
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
num_outputs = tensor_slice_len // batch_size
verify_fn(
    self, lambda: self._build_dataset(15.0, tensor_slice_len, batch_size,
                                      options), num_outputs)
