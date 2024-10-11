# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def computation():
    exit(random_ops.random_gamma([10], [0.5, 1.5]))

exit(strategy.run(computation))
