# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
shape = (1, 3)
dtype = dtypes.int32
trainable = False
alias_id = None
spec = resource_variable_ops.VariableSpec(shape, dtype, trainable)
spec_hash = hash(spec)
expected_hash = hash((shape, dtype, trainable, alias_id))
self.assertEqual(spec_hash, expected_hash)
