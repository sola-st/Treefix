control_cache = type('MockControlCache', (object,), {'get_control_outputs': lambda self, op: [op]})() # pragma: no cover
side_effects = [lambda x: [x * 2]] # pragma: no cover

class MockOperation: # pragma: no cover
    def __init__(self, name): # pragma: no cover
        self.name = name # pragma: no cover
        self.inputs = [] # pragma: no cover
        self.control_inputs = [] # pragma: no cover
    def consumers(self): # pragma: no cover
        return [self] # pragma: no cover
    def _update_input(self, index, tensor): pass # pragma: no cover
    def _remove_all_control_inputs(self): pass # pragma: no cover
    def _add_control_inputs(self, control_inputs): pass # pragma: no cover
control_cache = type('MockControlOutputCache', (object,), {'get_control_outputs': lambda self, op: []})() # pragma: no cover
ops = type('MockOps', (object,), {'name_scope': lambda name: (lambda: None), 'control_dependencies': lambda outs: (lambda: None)})() # pragma: no cover
side_effects = [lambda t: [t * 2]] # pragma: no cover
array_ops = type('MockArrayOps', (object,), {'identity': lambda t: t})() # pragma: no cover

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
_l_(7860)
for consumer_op in list(tensor.consumers()):
    _l_(7862)

    update_input.append((consumer_op, list(consumer_op.inputs).index(tensor)))
    _l_(7861)

update_control_input = control_cache.get_control_outputs(tensor.op)
_l_(7863)

# Trailing slash on name scope to replace the scope.
name_scope = tensor.op.name + '/subscription/'
_l_(7864)
with ops.name_scope(name_scope):
    _l_(7870)

    outs = []
    _l_(7865)
    for s in side_effects:
        _l_(7867)

        outs += s(tensor)
        _l_(7866)

    with ops.control_dependencies(outs):
        _l_(7869)

        out = array_ops.identity(tensor)
        _l_(7868)

for consumer_op, index in update_input:
    _l_(7872)

    consumer_op._update_input(index, out)  # pylint: disable=protected-access
    _l_(7871)  # pylint: disable=protected-access

for consumer_op in update_control_input:
    _l_(7879)

    # If an op has more than one output and two or more of its output tensors
    # are subscribed at the same time, we remove the control dependency from
    # the original op only once and we add the dependencies to all the
    # new identities.
    new_control_inputs = consumer_op.control_inputs
    _l_(7873)
    if tensor.op in new_control_inputs:
        _l_(7875)

        new_control_inputs.remove(tensor.op)
        _l_(7874)
    new_control_inputs.append(out.op)
    _l_(7876)
    # pylint: disable=protected-access
    consumer_op._remove_all_control_inputs()
    _l_(7877)
    consumer_op._add_control_inputs(new_control_inputs)
    _l_(7878)
aux = out
_l_(7880)
exit(aux)
