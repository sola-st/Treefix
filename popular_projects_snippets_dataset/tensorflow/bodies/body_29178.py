# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
x = constant_op.constant(1.0)
opt = optional_ops.Optional.from_value(x)
# TODO(skyewm): support returning Optionals from functions?
exit(opt._variant_tensor)
