# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def step_fn():
    v.assign_add(1)

for _ in math_ops.range(2):
    strategy.run(step_fn)
