# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Apply gradients to a replica variable."""
assert v is not None

try:
    # Convert the grad to Tensor or IndexedSlices if necessary.
    g = ops.convert_to_tensor_or_indexed_slices(g)
except TypeError:
    raise TypeError("Gradient must be convertible to a Tensor"
                    " or IndexedSlices, or None: %s" % g)
if not isinstance(g, (ops.Tensor, indexed_slices.IndexedSlices)):
    raise TypeError(
        "Gradient must be a Tensor, IndexedSlices, or None: %s" % g)
p = _get_processor(v)

if context.executing_eagerly() or (
    resource_variable_ops.is_resource_variable(v) and
    not v._in_graph_mode):  # pylint: disable=protected-access
    scope_name = v.name.split(":")[0]
else:
    scope_name = v.op.name

# device_policy is set because non-mirrored tensors will be read in
# `update_op`. `_resource_apply_dense`, `lr_t`, `beta1_t` and `beta2_t`
# is an example.
with ops.name_scope("update_" + scope_name):
    exit(p.update_op(self, g))
