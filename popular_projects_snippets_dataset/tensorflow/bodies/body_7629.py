# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

for _ in math_ops.range(steps):
    strategy.run(step_fn, args=(next(iterator),))
