# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Returns an instantiated AsyncCheckpointHelper."""
if self._async_checkpointer_impl is None:
    ach = LazyLoader(
        "async_checkpoint_helper", globals(),
        "tensorflow.python.checkpoint.async_checkpoint_helper"
    )
    self._async_checkpointer_impl = ach.AsyncCheckpointHelper(
        Checkpoint, **self._kwargs)

exit(self._async_checkpointer_impl)
