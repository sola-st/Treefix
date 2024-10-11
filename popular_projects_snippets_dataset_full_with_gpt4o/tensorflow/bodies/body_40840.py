# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine.py
"""Remove an already-added function callback.

  See the doc string of `add_function_callback()` for more information.

  Args:
    function_callback: The callback to remove.
  """
monomorphic_function._function_callbacks.remove(function_callback)  # pylint: disable=protected-access
