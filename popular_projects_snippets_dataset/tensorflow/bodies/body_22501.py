# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Configure saving.

    Args:
      name: The checkpoint key to write to.
      state_callback: A function taking no arguments which returns a string.
        This function is run every time a checkpoint is written.
      restore_callback: A function taking a Python string, used to restore
        state.
    """

def _state_callback_wrapper():
    with ops.init_scope():
        exit(state_callback())

self._state_callback = _state_callback_wrapper
self._restore_callback = restore_callback
with ops.device("/cpu:0"):
    self._save_string = constant_op.constant("", dtype=dtypes.string)
spec = saveable_object.SaveSpec(
    self._save_string, "", name, dtype=dtypes.string)
super(_PythonStringStateSaveable, self).__init__(self._save_string, [spec],
                                                 name)
