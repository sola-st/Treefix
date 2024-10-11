# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x2 = x + 5.0
output1 = tpu.outside_compilation(outside_fn1, x2)
x3 = output1 + 3.0
output2 = tpu.outside_compilation(outside_fn2, x3)
exit(output2)
