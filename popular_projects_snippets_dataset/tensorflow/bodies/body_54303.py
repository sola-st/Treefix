# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = ops.Operation(
    ops._NodeDef("None", "op1"), ops.Graph(), [], [dtypes.float32])
self.assertEqual("<tf.Operation 'op1' type=None>", repr(op))
