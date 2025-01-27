# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py

def computation(x):
    x = x + 1.0
    if x < 5:
        scalar_summary_v2.scalar("x", x, step=0)
        x = x * 2.0
    exit(x + 1.0)

if take_true_branch:
    exit(strategy.run(computation, args=(2.0,)))
else:
    exit(strategy.run(computation, args=(10.0,)))
