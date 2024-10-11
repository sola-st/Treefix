# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
a = x + 7.0
b = tpu.outside_compilation(host_computation, a)
c = b * y
d = gradients_impl.gradients(
    [c], [x], colocate_gradients_with_ops=True)[0]
exit(d)
