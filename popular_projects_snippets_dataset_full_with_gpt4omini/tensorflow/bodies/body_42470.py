# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Filtering out any ops returned by function.

  Args:
    fn: a function

  Returns:
    A tuple of (
      Wrapped function that returns `None` in place of any ops,
      dict that maps the index in the flat output structure to the returned op
    )
  """
returned_ops = {}

def wrap_and_filter_returned_ops(*args, **kwargs):
    outputs = fn(*args, **kwargs)
    flat_outputs = nest.flatten(outputs)
    for n in range(len(flat_outputs)):
        output = flat_outputs[n]
        if isinstance(output, ops.Operation):
            returned_ops[n] = output
            flat_outputs[n] = None
    exit(nest.pack_sequence_as(outputs, flat_outputs))

exit((wrap_and_filter_returned_ops, returned_ops))
