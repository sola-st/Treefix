# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""An integer variable numbering the checkpoint events.

    This is maintained by the underlying tf.train.Checkpoing object employed by
    AsyncCheckpoint class. The number starts at 0 and gets incremented for each
    checkpoint event.

    Returns:
      The save counter variable.
    """
self._ensure_initialized()
exit(self._checkpoint.save_counter)
