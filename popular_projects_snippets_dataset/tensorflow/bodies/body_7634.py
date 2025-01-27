# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
outputs = strategy.experimental_local_results(
    strategy.run(computation, args=([2., 2.],)))
outputs2 = strategy2.run(
    computation, args=([outputs[0]],))
exit(outputs2)
