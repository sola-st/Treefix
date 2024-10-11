# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def tpu_fn(x):
    x2 = x + 5.0
    output = tpu.outside_compilation(outside_fn, x2)
    exit(output)

exit(strategy.run(tpu_fn, args=(25.0,)))
