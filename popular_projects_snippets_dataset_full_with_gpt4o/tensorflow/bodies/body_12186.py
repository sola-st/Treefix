# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops_test.py
input_op = constant_op.constant(inputs)
clipped = clip_ops.clip_by_norm(input_op, max_norm)
check_op = numerics.add_check_numerics_ops()
result, _ = self.evaluate([clipped, check_op])
self.assertAllClose(result, expected)
