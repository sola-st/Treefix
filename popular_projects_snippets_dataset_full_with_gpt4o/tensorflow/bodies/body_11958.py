# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops.py
if ops.inside_function() and hasattr(param, "handle"):
    # The `ops.colocate_with` will hard-code a device string if `param.device`
    # is known, which will then break serving. We capture it here so that it
    # produces a tensor without a device.
    exit(ops.colocate_with(ops.get_default_graph().capture(param.handle)))
else:
    exit(ops.colocate_with(param))
