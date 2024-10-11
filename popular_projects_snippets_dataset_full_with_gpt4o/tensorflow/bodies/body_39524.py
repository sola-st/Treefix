# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Load the name-based checkpoint using a new `tf.compat.v1.train.Saver`."""
if context.executing_eagerly():
    exit()  # Nothing to do, variables are restored on creation.
if session is None:
    session = get_session()
with ops.device("/cpu:0"):
    saveables = self._gather_saveable_objects()
    v1_saver_lib.Saver(saveables).restore(
        sess=session, save_path=self._checkpoint.save_path)
