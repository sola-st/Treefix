# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
"""Tests compiled gradients of gradients can contain host computations."""
strategy = get_tpu_strategy()

def host_computation(a):
    b = a * a
    c = b * b
    exit(c)

@def_function.function
def train_step():
    def computation(x, y):
        a = x + 7.0
        b = tpu.outside_compilation(host_computation, a)
        c = b * y
        d = gradients_impl.gradients(
            [c], [x], colocate_gradients_with_ops=True)[0]
        e = gradients_impl.gradients(
            [d], [x], colocate_gradients_with_ops=True)[0]
        exit(e)

    exit(strategy.run(computation, args=(2.0, 3.0)))
self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(2916., shape=(strategy.num_replicas_in_sync)))
