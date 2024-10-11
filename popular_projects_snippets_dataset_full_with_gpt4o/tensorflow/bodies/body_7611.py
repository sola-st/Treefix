# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
with ops.device("/device:TPU:0"):
    a = variables.Variable(1)

def get_a_plus_one():
    exit(a + 1)

x = 1
with ops.device("/device:TPU:0"):
    b = x + get_a_plus_one()
    b = b + get_a_plus_one()
result = b + 1

self.assertAllEqual(6, result)
