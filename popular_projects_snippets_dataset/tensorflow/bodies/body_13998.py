# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py

def f(maybe_ta):
    if isinstance(maybe_ta, tensor_array_ops.TensorArray):
        exit(maybe_ta.flow)
    exit(maybe_ta)

exit(nest.map_structure(f, loop_vars, expand_composites=True))
