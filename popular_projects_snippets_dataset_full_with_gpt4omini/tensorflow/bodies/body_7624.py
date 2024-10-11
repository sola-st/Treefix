# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
with ops.device("/device:TPU:0"):
    where_output = array_ops.where([True, False, True])
self.assertAllEqual(where_output, [[0], [2]])

with ops.device("/device:TPU:0"):
    repeat_output = array_ops.repeat(math_ops.range(2), [1, 4])
self.assertAllEqual(repeat_output, [0, 1, 1, 1, 1])
