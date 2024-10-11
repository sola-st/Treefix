# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def step_fn():
    exit(v + 1.0)

all_core_strategy.run(step_fn)
r1 = first_core_strategy.run(step_fn)
r2 = second_core_strategy.run(step_fn)
exit(r1 + r2)
