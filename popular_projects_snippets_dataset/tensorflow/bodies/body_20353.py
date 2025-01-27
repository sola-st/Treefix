# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

@def_function.function
def computation(x):
    x = x + 1.0
    y = host_computation(x)
    exit(y + 1.0)

exit(strategy.run(computation, args=(2.0,)))
