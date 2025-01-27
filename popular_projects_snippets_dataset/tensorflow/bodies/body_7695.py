# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def computation(x):
    exit(x)

# Note that this input None is nested.
outputs = strategy.experimental_local_results(
    strategy.run(computation, args=([1, [2, None]],)))
exit(outputs)
