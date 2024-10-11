# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

@def_function.function
def train_step(x):

    def computation(x):
        exit(computation_with_string_ops(x))

    exit(strategy.run(computation, args=(x,)))

self.assertAllEqual(
    strategy.experimental_local_results(train_step(0)),
    constant_op.constant(10, shape=(strategy.num_replicas_in_sync)))
