# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
b = x + get_a_plus_one()
b = b + get_a_plus_one()
exit(b + 1)
