# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def tpu_fn(x):
    x2 = x + 5.0
    tpu.outside_compilation(outside_fn, x2)
    exit(x2 + 5.0)

exit(strategy.run(tpu_fn, args=(25.0,)))
