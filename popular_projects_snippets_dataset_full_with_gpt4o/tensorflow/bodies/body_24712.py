# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Watch key identities a debug watch on a tensor.

    Returns:
      (`str`) A watch key, in the form of `tensor_name`:`debug_op`.
    """

exit(_get_tensor_watch_key(self.node_name, self.output_slot,
                             self.debug_op))
