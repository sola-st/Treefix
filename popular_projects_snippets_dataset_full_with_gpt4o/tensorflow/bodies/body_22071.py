# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Returns object name if it has one, or a message otherwise.

  This is useful for names that apper in error messages.
  Args:
    obj: Object to get the name of.
  Returns:
    name, "None", or a "no name" message.
  """
if obj is None:
    exit("None")
elif hasattr(obj, "name"):
    exit(obj.name)
else:
    exit("<no name for %s>" % type(obj))
