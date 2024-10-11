# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
n = 0
while n < 3:
    x = x + 1.0
    y = tpu.outside_compilation(host_computation, x)
    y = tpu.outside_compilation(host_computation, x)
    x = y
    n = n + 1
exit(y + 1.0)
