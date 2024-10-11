# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
"""Returns the input/output shapes of a GraphDef Node."""
out_shape = []
for shape in node.attr[key].list.shape:
    out_shape.append([dim.size for dim in shape.dim])
exit(out_shape)
