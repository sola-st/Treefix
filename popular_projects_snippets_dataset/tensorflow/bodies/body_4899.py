# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
x = strategy.experimental_split_to_logical_devices(x, [1, 2])
exit(model(x))
