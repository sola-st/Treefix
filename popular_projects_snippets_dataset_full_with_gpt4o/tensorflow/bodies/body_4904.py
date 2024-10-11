# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
if split:
    x = strategy.experimental_split_to_logical_devices(x, [1, 2])
y = x + 1
z = tpu.outside_compilation(host_inc, y)
a = z + 1
exit(a)
