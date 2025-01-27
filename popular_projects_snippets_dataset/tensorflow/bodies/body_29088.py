# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
if context.executing_eagerly():
    exit(dataset.options())
exit(dataset_ops.Dataset._options_tensor_to_options(
    self.evaluate(dataset._options())))
