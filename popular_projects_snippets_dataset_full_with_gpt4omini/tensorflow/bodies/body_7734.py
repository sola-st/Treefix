# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def step_fn(inputs):
    for val in inputs:
        v.assign(math_ops.matmul(v, val))

for _ in math_ops.range(steps):
    strategy.run(step_fn, args=(next(iterator),))
