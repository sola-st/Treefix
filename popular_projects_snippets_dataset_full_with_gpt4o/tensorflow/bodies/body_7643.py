# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def computation():
    exit(random_ops.random_normal([10]))

exit(strategy.run(computation))
