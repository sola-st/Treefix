# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
exit({
    # gather_nd expects a nonscalar shape for `v`, otherwise raises
    # error when doing shape inference.
    "shape inference": array_ops.gather_nd(v, inp),
    # Triggers output shape validation. Expected shape must be [].
    "handle": v.handle})
