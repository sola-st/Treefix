# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x2 = x + 5.0
output = tpu.outside_compilation(outside_fn, x2)
exit(output)
