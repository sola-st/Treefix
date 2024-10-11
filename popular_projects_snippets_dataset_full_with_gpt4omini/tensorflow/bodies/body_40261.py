# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Ensures that `tensor` is being traced by this tape.

    Args:
      tensor: a Tensor/Variable or list of Tensors/Variables.

    Raises:
      ValueError: if it encounters something that is not a tensor.
    """
for t in _extract_tensors_and_variables(tensor):
    if not backprop_util.IsTrainable(t):
        logging.log_first_n(
            logging.WARN, "The dtype of the watched tensor must be "
            "floating (e.g. tf.float32), got %r", 5, t.dtype)
    if hasattr(t, "handle"):
        # There are many variable-like objects, all of them currently have
        # `handle` attribute that points to a tensor. If this changes,
        # internals of watch_variable need to change as well.
        tape.watch_variable(self._tape, t)
    else:
        tape.watch(self._tape, t)
