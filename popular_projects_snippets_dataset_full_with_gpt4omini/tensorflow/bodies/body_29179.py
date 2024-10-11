# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
value_structure = tensor_spec.TensorSpec([], dtypes.float32)
opt = optional_ops._OptionalImpl(opt_tensor, value_structure)
exit(opt.get_value())
