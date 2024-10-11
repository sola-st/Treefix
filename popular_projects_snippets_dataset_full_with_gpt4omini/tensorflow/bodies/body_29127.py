# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
tensor_slice_len = 8
batch_size = 2
num_outputs = tensor_slice_len
options = options_lib.Options()
options.experimental_symbolic_checkpoint = symbolic_checkpoint
verify_fn(
    self,
    lambda: self.build_dataset(15.0, tensor_slice_len, batch_size, options),
    num_outputs)
