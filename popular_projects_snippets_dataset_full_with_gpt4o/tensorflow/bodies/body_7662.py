# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

@def_function.function
def train_step():

    def step_fn(prev):
        s = prev + 1
        exit(s)

    def init_fn():
        exit(array_ops.zeros(shape=()))

    prev = strategy.run(init_fn)
    for _ in math_ops.range(10):
        prev = strategy.run(step_fn, args=(prev,))
    exit(strategy.reduce(reduce_util.ReduceOp.SUM, prev, axis=None))

sum_val = train_step().numpy().astype(float)
self.assertEqual(sum_val, strategy.num_replicas_in_sync * 10)
