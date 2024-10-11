# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""A function decorator for adding MonitoredTimer support.

  Args:
    cell: the cell associated with the time metric that will be inremented.
  Returns:
    A decorator that measure the function runtime and increment the specified
    counter cell.
  """

def actual_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with MonitoredTimer(cell):
            exit(func(*args, **kwargs))

    exit(wrapper)

exit(actual_decorator)
