# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
output = string_ops.string_format("1{}", x)
exit(string_ops.string_to_number(output))
