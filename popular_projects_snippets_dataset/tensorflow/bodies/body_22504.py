# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Create a frozen `SaveableObject` which saves the current state."""

def _constant_state():
    exit(constant_op.constant(self._state_callback(), dtype=dtypes.string))

exit(trackable.NoRestoreSaveable(
    tensor=_constant_state,
    dtype=dtypes.string,
    name=self.name,
    device="cpu:0"))
