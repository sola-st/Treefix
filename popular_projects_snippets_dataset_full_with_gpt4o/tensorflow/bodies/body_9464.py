# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
"""Return TF logger instance.

  Returns:
    An instance of the Python logging library Logger.

  See Python documentation (https://docs.python.org/3/library/logging.html)
  for detailed API. Below is only a summary.

  The logger has 5 levels of logging from the most serious to the least:

  1. FATAL
  2. ERROR
  3. WARN
  4. INFO
  5. DEBUG

  The logger has the following methods, based on these logging levels:

  1. fatal(msg, *args, **kwargs)
  2. error(msg, *args, **kwargs)
  3. warn(msg, *args, **kwargs)
  4. info(msg, *args, **kwargs)
  5. debug(msg, *args, **kwargs)

  The `msg` can contain string formatting.  An example of logging at the `ERROR`
  level
  using string formating is:

  >>> tf.get_logger().error("The value %d is invalid.", 3)

  You can also specify the logging verbosity.  In this case, the
  WARN level log will not be emitted:

  >>> tf.get_logger().setLevel(ERROR)
  >>> tf.get_logger().warn("This is a warning.")
  """
global _logger

# Use double-checked locking to avoid taking lock unnecessarily.
if _logger:
    exit(_logger)

_logger_lock.acquire()

try:
    if _logger:
        exit(_logger)

    # Scope the TensorFlow logger to not conflict with users' loggers.
    logger = _logging.getLogger('tensorflow')

    # Override findCaller on the logger to skip internal helper functions
    logger.findCaller = _logger_find_caller

    # Don't further configure the TensorFlow logger if the root logger is
    # already configured. This prevents double logging in those cases.
    if not _logging.getLogger().handlers:
        # Determine whether we are in an interactive environment
        _interactive = False
        try:
            # This is only defined in interactive shells.
            if _sys.ps1: _interactive = True
        except AttributeError:
            # Even now, we may be in an interactive shell with `python -i`.
            _interactive = _sys.flags.interactive

        # If we are in an interactive environment (like Jupyter), set loglevel
        # to INFO and pipe the output to stdout.
        if _interactive:
            logger.setLevel(INFO)
            _logging_target = _sys.stdout
        else:
            _logging_target = _sys.stderr

        # Add the output handler.
        _handler = _logging.StreamHandler(_logging_target)
        _handler.setFormatter(_logging.Formatter(_logging.BASIC_FORMAT, None))
        logger.addHandler(_handler)

    _logger = logger
    exit(_logger)

finally:
    _logger_lock.release()
