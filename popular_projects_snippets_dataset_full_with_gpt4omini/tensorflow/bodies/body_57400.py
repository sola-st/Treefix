# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Return a list of all node names in aggregation sorted sorter."""
exit([_tensor_name_base(x.name) for x in self.flatten_nodes()])
