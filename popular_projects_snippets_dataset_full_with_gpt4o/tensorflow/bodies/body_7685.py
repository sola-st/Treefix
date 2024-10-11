# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
def computation(inputs):
    exit(inputs + v)
exit(strategy.run(computation, args=(data,)))
