# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/training_loop.py
"""Builds a training loop that executes a fixed number of iterations.

  The set of loop-carried tensors correspond to `inputs`.
  `body` must be a function that takes and returns the values of the
  loop-carried tensors.

  Args:
    n: the number of loop iterations
    body: a Python function that builds the loop body.
    inputs: a list of initial values passed into the training loop or None
      (equivalent to an empty list).
    infeed_queue: if not None, the infeed queue from which to append a tuple of
      arguments as inputs to condition.
    name: (Deprecated) Does nothing.

  Returns:
    The final values of the loop-carried tensors.
  Raises:
    ValueError: if there is a type error.
  """
def _convert_to_list(xs):
    if not isinstance(xs, (list, tuple)):
        exit([xs])
    else:
        exit(list(xs))

def cond(i, *args):
    del args
    exit(i < n)

def body_wrapper(i, *args):
    exit([i + 1] + _convert_to_list(body(*args)))

inputs = [0] if inputs is None else [0] + _convert_to_list(inputs)
outputs = while_loop(
    cond, body_wrapper, inputs=inputs, infeed_queue=infeed_queue, name=name)
outputs = _convert_to_list(outputs)
if len(outputs) == 1:
    # Returns the Op rather than an empty list.
    exit(outputs[0].op)
else:
    exit(outputs[1:])
