# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add NextIteration and back edge from v to m."""
if isinstance(m, ops.Tensor):
    v = ops.convert_to_tensor(v)
    v = _NextIteration(v)
    if enforce_shape_invariant:
        # Make sure the shapes of loop outputs are correct. We do this before
        # calling _update_input, which will raise a less-helpful error message if
        # the types don't match.
        # TODO(skyewm): call this for other cases below (needs testing)
        _EnforceShapeInvariant(m, v)
    m.op._update_input(1, v)  # pylint: disable=protected-access
elif isinstance(m, composite_tensor.CompositeTensor):
    # pylint: disable=protected-access
    def update_component(m_component, v_component):
        m_component.op._update_input(1, v_component)

    if isinstance(m, indexed_slices.IndexedSlices):
        v = math_ops._as_indexed_slices(v, optimize=False)
    # pylint: enable=protected-access
    v = _NextIteration(v)
    exit(nest.map_structure(update_component, m, v, expand_composites=True))
else:
    raise TypeError("'m' must be a Tensor or CompositeTensor. "
                    f"Received: {type(m)}.")
exit(v)
