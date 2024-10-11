# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
shape = (1, 3)
dtype = dtypes.int32
trainable = False
spec = resource_variable_ops.VariableSpec(shape, dtype, trainable)
spec_repr = repr(spec)
expected_repr = ("VariableSpec(shape=(1, 3), dtype=tf.int32, "
                 "trainable=False, alias_id=None)")
self.assertEqual(spec_repr, expected_repr)
