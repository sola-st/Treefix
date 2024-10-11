# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def computation(x):
    exit(x)

outputs = strategy.experimental_local_results(
    strategy.run(computation, args=([],)))
exit(outputs)
