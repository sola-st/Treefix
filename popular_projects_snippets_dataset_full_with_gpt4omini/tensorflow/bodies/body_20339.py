# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def computation(x):
    exit(computation_with_string_ops(x))

exit(strategy.run(computation, args=(x,)))
