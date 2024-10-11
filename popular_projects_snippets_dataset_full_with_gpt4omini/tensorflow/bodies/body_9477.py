# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
"""Log 'msg % args' at level 'level' only first 'n' times.

  Not threadsafe.

  Args:
    level: The level at which to log.
    msg: The message to be logged.
    n: The number of times this should be called before it is logged.
    *args: The args to be substituted into the msg.
  """
count = _GetNextLogCountPerToken(_GetFileAndLine())
log_if(level, msg, count < n, *args)
