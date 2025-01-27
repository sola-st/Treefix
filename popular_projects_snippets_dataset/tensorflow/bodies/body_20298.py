# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

def outside_fn(x):
    logging_ops.print_v2("Outside compiled", x)
    exit(x + 6.0)

input_value = 51.0 if take_true_branch else 25.0

@def_function.function
def train_step():

    def tpu_fn(x):
        x2 = x + 5.0
        if x < 50.0:
            exit(tpu.outside_compilation(outside_fn, x2))
        else:
            exit(x2)

    exit(strategy.run(tpu_fn, args=(input_value,)))

output_value = 36.0
if take_true_branch:
    output_value = 56.0
self.assertAllEqual(
    strategy.experimental_local_results(train_step()),
    constant_op.constant(
        output_value, shape=(strategy.num_replicas_in_sync)))
