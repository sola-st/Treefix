# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Convert a TensorHandle object to a feedable numpy value.

    Returns:
      A numpy array of a custom struct type that can be used as a feed value
      to run().
    """
exit(encode_resource_handle(self._get_resource_handle()))
