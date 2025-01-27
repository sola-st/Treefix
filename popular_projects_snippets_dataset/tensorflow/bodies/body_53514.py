# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Common logic for creating an op in this graph."""
# Apply any additional attributes requested. Do not overwrite any existing
# attributes.
for key, value in self._attr_scope_map.items():
    try:
        op.get_attr(key)
    except ValueError:
        if callable(value):
            value = value(op.node_def)
            if not isinstance(value, (type(None), attr_value_pb2.AttrValue)):
                raise TypeError(
                    "Callable for scope map key '%s' must return either None or "
                    "an AttrValue protocol buffer; but it returned: %s" %
                    (key, value))
        if value:
            op._set_attr(key, value)  # pylint: disable=protected-access

    # Apply a kernel label if one has been specified for this op type.
try:
    kernel_label = self._op_to_kernel_label_map[op.type]
    op._set_attr("_kernel",  # pylint: disable=protected-access
                 attr_value_pb2.AttrValue(s=compat.as_bytes(kernel_label)))
except KeyError:
    pass

op._gradient_function = self._gradient_function_map.get(op.type)  # pylint: disable=protected-access

# Apply the overriding op type for gradients if one has been specified for
# this op type.
try:
    mapped_op_type = self._gradient_override_map[op.type]
    op._set_attr("_gradient_op_type",  # pylint: disable=protected-access
                 attr_value_pb2.AttrValue(s=compat.as_bytes(mapped_op_type)))
except KeyError:
    pass

self._record_op_seen_by_control_dependencies(op)

if compute_device:
    self._apply_device_functions(op)

# Snapshot the colocation stack metadata before we might generate error
# messages using it.  Note that this snapshot depends on the actual stack
# and is independent of the op's _class attribute.
# pylint: disable=protected-access
op._colocation_code_locations = self._snapshot_colocation_stack_metadata()
# pylint: enable=protected-access

if self._colocation_stack:
    all_colocation_groups = []
    is_device_set = False
    for colocation_op in self._colocation_stack.peek_objs():
        try:
            all_colocation_groups.extend(colocation_op.colocation_groups())
        except AttributeError:
            pass
        if colocation_op.device and not is_device_set:
            # pylint: disable=protected-access
            op._set_device(colocation_op.device)
            # pylint: enable=protected-access
            is_device_set = True

    all_colocation_groups = sorted(set(all_colocation_groups))
    # pylint: disable=protected-access
    op._set_attr(
        "_class",
        attr_value_pb2.AttrValue(
            list=attr_value_pb2.AttrValue.ListValue(s=all_colocation_groups)))
    # pylint: enable=protected-access

# Sets "container" attribute if
# (1) self._container is not None
# (2) "is_stateful" is set in OpDef
# (3) "container" attribute is in OpDef
# (4) "container" attribute is None
if self._container and op._is_stateful:  # pylint: disable=protected-access
    try:
        container_attr = op.get_attr("container")
    except ValueError:
        # "container" attribute is not in OpDef
        pass
    else:
        if not container_attr:
            op._set_attr("container", attr_value_pb2.AttrValue(  # pylint: disable=protected-access
                s=compat.as_bytes(self._container)))
