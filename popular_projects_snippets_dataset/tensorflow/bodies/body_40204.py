# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
# Like for Identity, this special case means we don't need to create
# variable-shaped Tensors from resource handles.
del attr_tuple, inputs, outputs
exit([array_ops.identity(t) for t in tangents])
