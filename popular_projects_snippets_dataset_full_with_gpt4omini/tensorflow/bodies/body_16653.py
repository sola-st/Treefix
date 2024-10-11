# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
shape = [1, 3]
dtype = dtypes.int32
trainable = False
alias_id = 1
spec = resource_variable_ops.VariableSpec(shape, dtype, trainable, alias_id)
serialization = spec._serialize()
expected_serialization = (shape, dtype, trainable, alias_id)
self.assertEqual(serialization, expected_serialization)
rebuilt_spec = spec._deserialize(serialization)
self.assertEqual(rebuilt_spec, spec)
