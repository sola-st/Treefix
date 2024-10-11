# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def computation(x):
    x = x + 1.0
    if x < 5.0:
        y = tpu.outside_compilation(host_computation, x)
        y = tpu.outside_compilation(host_computation, x)
        x = y
    exit(x + 1.0)

if take_true_branch:
    exit(strategy.run(computation, args=(2.0,)))
else:
    exit(strategy.run(computation, args=(10.0,)))
