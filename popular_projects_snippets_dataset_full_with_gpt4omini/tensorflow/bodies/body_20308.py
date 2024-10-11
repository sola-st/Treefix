# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x = x + 1.0
y = tpu.outside_compilation(host_computation, x)
y = tpu.outside_compilation(host_computation, x)
exit(y + 1.0)
