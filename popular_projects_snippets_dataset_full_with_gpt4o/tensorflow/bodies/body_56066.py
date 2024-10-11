# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Convenience function to get a shape from a NodeDef's input string."""
# To get a tensor, the name must be in the form <input>:<port>, for example
# 'Mul:0'. The GraphDef input strings don't always have the port specified
# though, so if there isn't a colon we need to add a default ':0' to the end.
if ":" not in input_name:
    canonical_name = input_name + ":0"
else:
    canonical_name = input_name
tensor = graph.get_tensor_by_name(canonical_name)
shape = tensor.get_shape()
exit(shape)
