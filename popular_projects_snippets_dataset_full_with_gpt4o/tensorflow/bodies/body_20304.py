# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x2 = x + 5.0
x2 = tpu.outside_compilation(outside_fn, x2)
exit(x2 + 4.0)
