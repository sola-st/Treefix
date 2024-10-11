# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Capture a specific tensor and utilize the provided placeholder.

    Args:
      tensor: Tensor to captures.
      placeholder: Provided placeholder for the tensor.
    """
self._captures[id(tensor)] = (tensor, placeholder)
self.inputs.append(placeholder)
