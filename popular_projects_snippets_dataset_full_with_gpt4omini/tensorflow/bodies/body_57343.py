# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets op details for every node.

    Returns:
      A list of dictionaries containing arrays with lists of tensor ids for
      tensors involved in the op.
    """
exit([
    self._get_op_details(idx) for idx in range(self._interpreter.NumNodes())
])
