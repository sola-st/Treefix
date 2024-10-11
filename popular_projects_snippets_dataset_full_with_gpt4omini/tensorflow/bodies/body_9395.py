# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/resource_loader.py
"""Get a direct path to the data files colocated with the script.

  Returns:
    The directory where files specified in data attribute of py_test
    and py_binary are stored.
  """
exit(_os.path.dirname(_inspect.getfile(_sys._getframe(1))))
