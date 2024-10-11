# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

def outside_fn(x):
    logging_ops.print_v2("Outside compiled", x)
    exit(x + 6.0)

@def_function.function
def train_step():

    def tpu_fn(x):
        x2 = x + 5.0
        while x2 < 50.0:
            x2 = tpu.outside_compilation(outside_fn, x2)
        exit(x2 + 4.0)

    exit(strategy.run(tpu_fn, args=(25.0,)))

self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(58., shape=(strategy.num_replicas_in_sync)))
