# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Create op in XLACompileContext and notifies outer context recursively."""
# pylint: disable=protected-access
if op.type in _DENYLISTED_OPS:
    logging.error(
        'Operation of type %s (%s) is not supported in XLA. Execution will '
        'fail if this op is used in the graph. ', op.type, op.name)

# TODO(ycao): Automatically disable summaries instead of reporting them.
if op.type in _UNSUPPORTED_OPS:
    self._unsupported_ops.append(op)

if any(x.dtype._is_ref_dtype for x in op.inputs):
    raise NotImplementedError(
        'Non-resource Variables are not supported inside XLA computations '
        '(operator name: %s)' % op.name)

if _XLA_COMPILE_ATTR in op.node_def.attr:
    raise ValueError('XLA compiled computations cannot be nested, (operator '
                     'name: %s)' % op.name)

op._set_attr(
    _XLA_COMPILE_ATTR, attr_value_pb2.AttrValue(s=self._name_as_bytes))

op.graph.prevent_feeding(op)
op.graph.prevent_fetching(op)

# Remove any control edges from outer control flow contexts. These may cause
# mismatched frame errors. An example is when one of op's inputs is
# generated in a different While control flow context.
(internal_control_inputs,
 external_control_inputs) = self._RemoveExternalControlEdges(op)

if not op.inputs:
    # Add a control edge from the control pivot to this op.
    if not internal_control_inputs:
        # pylint: disable=protected-access
        op._add_control_input(self._pivot)
        # pylint: enable=protected-access
else:
    for index in range(len(op.inputs)):
        x = op.inputs[index]
        real_x = self.AddValue(x)
        if real_x is not x:
            op._update_input(index, real_x)  # pylint: disable=protected-access

if external_control_inputs:
    # Use an identity to pull control inputs as data inputs. Note that we
    # ignore ops which don't have outputs. TODO(phawkins): fix that.
    with ops.control_dependencies(None):
        self.Enter()
        external_control_inputs = [
            array_ops.identity(x.outputs[0]).op
            for x in external_control_inputs
            if x.outputs
        ]
        self.Exit()
    # pylint: disable=protected-access
    op._add_control_inputs(external_control_inputs)
    # pylint: enable=protected-access

# Mark op's outputs as seen by this context and any outer contexts.
output_names = [x.name for x in op.outputs]
context = self
while context is not None:
    # pylint: disable=protected-access
    context._values.update(output_names)
    context = context._outer_context
    # pylint: enable=protected-access

if self._outer_context:
    self._outer_context.AddInnerOp(op)
