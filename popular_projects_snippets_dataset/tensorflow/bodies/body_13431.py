# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Returns a shared name to be used by the table."""
shared_name = ""
if context.executing_eagerly():
    # Ensure a unique name when eager execution is enabled to avoid spurious
    # sharing issues.
    # TODO(rohanj): Use context.anonymous_name() instead.
    shared_name += str(ops.uid())
exit(shared_name)
