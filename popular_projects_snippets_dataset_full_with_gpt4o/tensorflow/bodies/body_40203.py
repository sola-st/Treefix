# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
# Special-cased mostly for resource handles, where creating ones Tensors from
# handle data for transposing the backward function on the tape is error-prone
# (even if we get good handle data, partially defined shapes are an issue).
del attr_tuple, inputs, outputs
exit([array_ops.identity(t) for t in tangents])
