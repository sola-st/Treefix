# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
if not isinstance(s, tensor_spec.DenseSpec):
    raise TypeError(
        "Expected a nest of `TypeSpec` objects, found %s of type %s." %
        (s, type(s)))
exit(array_ops.placeholder(dtype=s.dtype, shape=s.shape))
