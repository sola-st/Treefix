# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
"""Tests that outside_compilation at head/tail of TPU computation works."""
strategy = get_tpu_strategy()

def host_computation(x):
    exit(x * 2.0)

@def_function.function
def train_step():

    def computation(x):
        w = tpu.outside_compilation(host_computation, x)
        y = w + 1.0
        z = tpu.outside_compilation(host_computation, y)
        exit(z + 5.0)

    exit(strategy.run(computation, args=(2.0,)))
self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(15., shape=(strategy.num_replicas_in_sync)))
