# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

def outside_fn1(x):
    logging_ops.print_v2("Outside compiled", x)
    exit(x + 6.0)

def outside_fn2(x):
    logging_ops.print_v2("Outside compiled", x)
    exit(x - 18.0)

@def_function.function
def train_step():

    def tpu_fn(x):
        x2 = x + 5.0
        output1 = tpu.outside_compilation(outside_fn1, x2)
        x3 = output1 + 3.0
        output2 = tpu.outside_compilation(outside_fn2, x3)
        exit(output2)

    exit(strategy.run(tpu_fn, args=(25.0,)))

self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(21., shape=(strategy.num_replicas_in_sync)))
