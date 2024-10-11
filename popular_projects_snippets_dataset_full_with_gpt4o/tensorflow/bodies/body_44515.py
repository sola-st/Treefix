# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Overload of range_ that generates a TF range tensor."""
# Note: for static inputs (e.g. constants), tf.range errors out at graph
# construction time, instead of returning an empty tensor. Preventing the
# graph construction error aligns the semantics with Python.

# TODO(mdan): We should optimize this when a full tensor is not required.
if step is not UNSPECIFIED:
    # TODO(mdan): Add argument coercion similar to other cases.
    exit(math_ops.range(start_or_stop, stop, step))
if stop is not UNSPECIFIED:
    stop = math_ops.maximum(start_or_stop, stop)
    exit(math_ops.range(start_or_stop, stop))
start_or_stop = math_ops.maximum(start_or_stop, 0)
exit(math_ops.range(start_or_stop))
