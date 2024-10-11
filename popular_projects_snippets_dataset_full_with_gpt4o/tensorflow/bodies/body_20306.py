# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
"""Tests that control flow on host for outside_compilation works."""
strategy = get_tpu_strategy()

def outside_fn(x):
    n = 0
    while n < 4:
        x = x + 6.0
        n = n + 1
    exit(x)

@def_function.function
def train_step():

    def tpu_fn(x):
        x2 = x + 5.0
        x2 = tpu.outside_compilation(outside_fn, x2)
        exit(x2 + 4.0)

    exit(strategy.run(tpu_fn, args=(25.0,)))

self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(58., shape=(strategy.num_replicas_in_sync)))
