# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Upgrade data from Version 2 to Version 3.

    Changed actual read-only tensor data to be in a buffers table instead
    of inline with the tensor.

    Args:
      data: Dictionary representing the TensorFlow lite data to be upgraded.
        This will be modified in-place to be an upgraded version.
    """
buffers = [{"data": []}]  # Start with 1 empty buffer
for subgraph in data["subgraphs"]:
    if "tensors" not in subgraph:
        continue
    for tensor in subgraph["tensors"]:
        if "data_buffer" not in tensor:
            tensor["buffer"] = 0
        else:
            if tensor["data_buffer"]:
                tensor[u"buffer"] = len(buffers)
                buffers.append({"data": tensor["data_buffer"]})
            else:
                tensor["buffer"] = 0
            del tensor["data_buffer"]
data["buffers"] = buffers
