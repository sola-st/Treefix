# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
outputs = strategy.experimental_local_results(
    strategy.run(computation, args=(2,)))
exit(outputs)
