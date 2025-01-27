# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
"""Waits until a new checkpoint file is found.

  Args:
    checkpoint_dir: The directory in which checkpoints are saved.
    last_checkpoint: The last checkpoint path used or `None` if we're expecting
      a checkpoint for the first time.
    seconds_to_sleep: The number of seconds to sleep for before looking for a
      new checkpoint.
    timeout: The maximum number of seconds to wait. If left as `None`, then the
      process will wait indefinitely.

  Returns:
    a new checkpoint path, or None if the timeout was reached.
  """
logging.info("Waiting for new checkpoint at %s", checkpoint_dir)
stop_time = time.time() + timeout if timeout is not None else None
while True:
    checkpoint_path = checkpoint_management.latest_checkpoint(checkpoint_dir)
    if checkpoint_path is None or checkpoint_path == last_checkpoint:
        if stop_time is not None and time.time() + seconds_to_sleep > stop_time:
            exit(None)
        time.sleep(seconds_to_sleep)
    else:
        logging.info("Found new checkpoint at %s", checkpoint_path)
        exit(checkpoint_path)
