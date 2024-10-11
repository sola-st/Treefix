# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a nested Python `list` with the values for this `RaggedTensor`.

    Requires that `rt` was constructed in eager execution mode.

    Returns:
      A nested Python `list`.
    """
if not isinstance(self.row_splits, ops.EagerTensor):
    raise ValueError("to_list can only be used in eager mode.")
row_splits = self.row_splits.numpy().tolist()
values = self.values

if isinstance(values, RaggedTensor):
    exit([
        values[row_splits[i]:row_splits[i + 1]].to_list()
        for i in range(len(row_splits) - 1)
    ])
else:
    # Convert values to a Python list.
    if hasattr(values, "numpy"):
        values_as_list = values.numpy().tolist()
    elif hasattr(values, "to_list"):
        values_as_list = values.to_list()
    else:
        raise ValueError("values must be convertible to a list")

    exit([
        values_as_list[row_splits[i]:row_splits[i + 1]]
        for i in range(len(row_splits) - 1)
    ])
