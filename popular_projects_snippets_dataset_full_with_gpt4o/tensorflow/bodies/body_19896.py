# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Generate enqueue ops for outside compilation."""
# Note that we put array_ops.where_v2 rather than a python if so that
# the op is explicitly create and the constant ops are both in the graph
# even though we don't expect training to be a tensor (and thus generate
# control flow automatically). This need to make it easier to re-write
# the graph later if we need to fix which mode needs to be used.
mode_override = array_ops.where_v2(training,
                                   constant_op.constant("train"),
                                   constant_op.constant("inference"))
# Device ordinal is -1 here, a later rewrite will fix this once the op
# is expanded by outside compilation.
enqueue_op = self._generate_enqueue_op(
    flat_inputs, flat_weights, flat_features, device_ordinal=-1,
    mode_override=mode_override)

# Apply the name tag to the op.
if name is not None:
    _add_key_attr(enqueue_op, name)
