# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
strategy, _ = get_tpu_strategy(enable_spmd=True)
x = constant_op.constant([0, 1])
with self.assertRaises(ValueError):
    strategy.experimental_assign_to_logical_device(x, 0)
