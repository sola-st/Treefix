# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Context manager to request stop when an Exception is raised.

    Code that uses a coordinator must catch exceptions and pass
    them to the `request_stop()` method to stop the other threads
    managed by the coordinator.

    This context handler simplifies the exception handling.
    Use it as follows:

    ```python
    with coord.stop_on_exception():
      # Any exception raised in the body of the with
      # clause is reported to the coordinator before terminating
      # the execution of the body.
      ...body...
    ```

    This is completely equivalent to the slightly longer code:

    ```python
    try:
      ...body...
    except:
      coord.request_stop(sys.exc_info())
    ```

    Yields:
      nothing.
    """
try:
    exit()
except:  # pylint: disable=bare-except
    self.request_stop(ex=sys.exc_info())
