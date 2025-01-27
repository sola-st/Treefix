# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
with ops.device("/device:TPU:0"):
    b = x + get_a_plus_one()
    b = b + get_a_plus_one()
exit(b + 1)
