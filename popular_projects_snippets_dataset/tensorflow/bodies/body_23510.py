# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state.py
"""Implements Trackable._serialize_to_tensors."""
with ops.init_scope():
    value = constant_op.constant(self.serialize(), dtype=dtypes.string)
exit({PYTHON_STATE: value})
