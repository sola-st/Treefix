# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x2 = x + 5.0
if x < 50.0:
    exit(tpu.outside_compilation(outside_fn, x2))
else:
    exit(x2)
