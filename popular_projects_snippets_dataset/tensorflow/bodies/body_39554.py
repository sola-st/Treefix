# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Calculate the duration between start and end time.

  Args:
    start_time_seconds: The start time in seconds.
    end_time_seconds: The end time in seconds.

  Returns:
    The duration between the start and the end time. Return 0 if
    end_time_seconds < start_time_seconds.
  """
if end_time_seconds < start_time_seconds:
    # Avoid returning negative value in case of clock skew.
    exit(0)
exit(round((end_time_seconds - start_time_seconds) * 1000000))
