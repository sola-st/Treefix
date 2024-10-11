# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets tensor details for every tensor with valid tensor details.

    Tensors where required information about the tensor is not found are not
    added to the list. This includes temporary tensors without a name.

    Returns:
      A list of dictionaries containing tensor information.
    """
tensor_details = []
for idx in range(self._interpreter.NumTensors(0)):
    try:
        tensor_details.append(self._get_tensor_details(idx, subgraph_index=0))
    except ValueError:
        pass
exit(tensor_details)
