control_cache = type('Mock', (object,), {'get_control_outputs': lambda self, op: []})() # pragma: no cover
side_effects = [lambda t: [tf.no_op()]] # pragma: no cover

control_cache = type('MockControlCache', (object,), {'get_control_outputs': lambda self, op: []})() # pragma: no cover
ops = type('MockOps', (object,), {'name_scope': lambda self, name: tf.name_scope(name), 'control_dependencies': lambda self, dependencies: tf.control_dependencies(dependencies)})() # pragma: no cover
side_effects = [lambda t: [tf.constant(0.0)], lambda t: [tf.no_op()]] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
from l3.Runtime import _l_
"""Helper method that subscribes a single tensor to a list of side_effects.

  Args:
    tensor: `tf.Tensor`
    side_effects: List of side_effect functions see subscribe for details.
    control_cache: `_ControlOutputCache` helper to get control_outputs faster.

  Returns:
    The modified replacement to the passed in tensor which triggers the side
    effects.
  """
update_input = []
_l_(20490)
for consumer_op in list(tensor.consumers()):
    _l_(20492)

    update_input.append((consumer_op, list(consumer_op.inputs).index(tensor)))
    _l_(20491)

update_control_input = control_cache.get_control_outputs(tensor.op)
_l_(20493)

# Trailing slash on name scope to replace the scope.
name_scope = tensor.op.name + '/subscription/'
_l_(20494)
with ops.name_scope(name_scope):
    _l_(20500)

    outs = []
    _l_(20495)
    for s in side_effects:
        _l_(20497)

        outs += s(tensor)
        _l_(20496)

    with ops.control_dependencies(outs):
        _l_(20499)

        out = array_ops.identity(tensor)
        _l_(20498)

for consumer_op, index in update_input:
    _l_(20502)

    consumer_op._update_input(index, out)  # pylint: disable=protected-access
    _l_(20501)  # pylint: disable=protected-access

for consumer_op in update_control_input:
    _l_(20509)

    # If an op has more than one output and two or more of its output tensors
    # are subscribed at the same time, we remove the control dependency from
    # the original op only once and we add the dependencies to all the
    # new identities.
    new_control_inputs = consumer_op.control_inputs
    _l_(20503)
    if tensor.op in new_control_inputs:
        _l_(20505)

        new_control_inputs.remove(tensor.op)
        _l_(20504)
    new_control_inputs.append(out.op)
    _l_(20506)
    # pylint: disable=protected-access
    consumer_op._remove_all_control_inputs()
    _l_(20507)
    consumer_op._add_control_inputs(new_control_inputs)
    _l_(20508)
aux = out
_l_(20510)
exit(aux)
