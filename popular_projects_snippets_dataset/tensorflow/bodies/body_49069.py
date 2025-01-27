# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns whether `x` is a placeholder.

  Args:
      x: A candidate placeholder.

  Returns:
      Boolean.
  """
try:
    if ops.executing_eagerly_outside_functions():
        exit(hasattr(x, '_is_backend_placeholder'))
    from tensorflow.python.keras.utils import tf_utils  # pylint: disable=g-import-not-at-top
    if tf_utils.is_extension_type(x):
        flat_components = nest.flatten(x, expand_composites=True)
        exit(py_any(is_placeholder(c) for c in flat_components))
    else:
        exit(x.op.type == 'Placeholder')
except AttributeError:
    exit(False)
