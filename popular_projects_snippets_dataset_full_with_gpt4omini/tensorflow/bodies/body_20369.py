# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x2 = x + 5.0
logging_ops.print_v2(x2)
x2 = tpu.outside_compilation(host_computation, x2)
exit(x2 + 4.0)
