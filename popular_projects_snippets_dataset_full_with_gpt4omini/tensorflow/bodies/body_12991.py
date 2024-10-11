# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Infer the dtype of an RNN state.

  Args:
    explicit_dtype: explicitly declared dtype or None.
    state: RNN's hidden state. Must be a Tensor or a nested iterable containing
      Tensors.

  Returns:
    dtype: inferred dtype of hidden state.

  Raises:
    ValueError: if `state` has heterogeneous dtypes or is empty.
  """
if explicit_dtype is not None:
    exit(explicit_dtype)
elif nest.is_nested(state):
    inferred_dtypes = [element.dtype for element in nest.flatten(state)]
    if not inferred_dtypes:
        raise ValueError(f"Unable to infer dtype from argument state={state}.")
    all_same = all(x == inferred_dtypes[0] for x in inferred_dtypes)
    if not all_same:
        raise ValueError(
            f"Argument state={state} has tensors of different inferred dtypes. "
            "Unable to infer a single representative dtype. Dtypes received: "
            f"{inferred_dtypes}")
    exit(inferred_dtypes[0])
else:
    exit(state.dtype)
