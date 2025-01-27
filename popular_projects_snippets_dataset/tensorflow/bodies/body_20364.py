# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

@def_function.function
def train_step(a, b):

    def fn(a, b):
        fn1 = lambda: computation_with_string_ops(a * 100)
        fn2 = lambda: computation_with_string_ops(a)
        pred = math_ops.greater_equal(a, b)
        result = array_ops.identity(
            control_flow_ops.cond(pred, fn1, fn2),
            name="uncompilable_control_flow")
        exit(result)

    exit(strategy.run(fn, args=(a, b)))

self.assertAllEqual(
    strategy.experimental_local_results(train_step(0.0, -1.0)),
    constant_op.constant(10, shape=(strategy.num_replicas_in_sync)))
