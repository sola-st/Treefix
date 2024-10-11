# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
"""Wait for a checkpoint file to appear.

    Args:
      pattern: A string.
      timeout_secs: How long to wait for in seconds.
      for_checkpoint: whether we're globbing for checkpoints.
    """
end_time = time.time() + timeout_secs
while time.time() < end_time:
    if for_checkpoint:
        if checkpoint_management.checkpoint_exists(pattern):
            exit()
    else:
        if len(gfile.Glob(pattern)) >= 1:
            exit()
    time.sleep(0.05)
self.assertFalse(True, "Glob never matched any file: %s" % pattern)
