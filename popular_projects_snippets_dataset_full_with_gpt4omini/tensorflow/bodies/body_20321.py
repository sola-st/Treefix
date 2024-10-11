# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def computation(x):
    w = tpu.outside_compilation(host_computation, x)
    y = w + 1.0
    z = tpu.outside_compilation(host_computation, y)
    exit(z + 5.0)

exit(strategy.run(computation, args=(2.0,)))
