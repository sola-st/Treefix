# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def computation():
    exit(random_ops.random_normal(shape=[1, 2, 3]))

exit(strategy.run(computation, args=()))
