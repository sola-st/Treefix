StackedRNNCells = lambda cell: cell # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
kwargs = {'zero_output_for_mask': False} # pragma: no cover
return_sequences = False # pragma: no cover
return_state = False # pragma: no cover
go_backwards = False # pragma: no cover
stateful = False # pragma: no cover
unroll = False # pragma: no cover
time_major = False # pragma: no cover
ds_context = type('MockContext', (object,), {'has_strategy': lambda self: False})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
from l3.Runtime import _l_
if isinstance(cell, (list, tuple)):
    _l_(5131)

    cell = StackedRNNCells(cell)
    _l_(5130)
if not 'call' in dir(cell):
    _l_(5133)

    raise ValueError('`cell` should have a `call` method. '
                     'The RNN was passed:', cell)
    _l_(5132)
if not 'state_size' in dir(cell):
    _l_(5135)

    raise ValueError('The RNN cell should have '
                     'an attribute `state_size` '
                     '(tuple of integers, '
                     'one integer per RNN state).')
    _l_(5134)
# If True, the output for masked timestep will be zeros, whereas in the
# False case, output from previous timestep is returned for masked timestep.
self.zero_output_for_mask = kwargs.pop('zero_output_for_mask', False)
_l_(5136)

if 'input_shape' not in kwargs and (
    'input_dim' in kwargs or 'input_length' in kwargs):
    _l_(5139)

    input_shape = (kwargs.pop('input_length', None),
                   kwargs.pop('input_dim', None))
    _l_(5137)
    kwargs['input_shape'] = input_shape
    _l_(5138)

super(RNN, self).__init__(**kwargs)
_l_(5140)
self.cell = cell
_l_(5141)
self.return_sequences = return_sequences
_l_(5142)
self.return_state = return_state
_l_(5143)
self.go_backwards = go_backwards
_l_(5144)
self.stateful = stateful
_l_(5145)
self.unroll = unroll
_l_(5146)
self.time_major = time_major
_l_(5147)

self.supports_masking = True
_l_(5148)
# The input shape is unknown yet, it could have nested tensor inputs, and
# the input spec will be the list of specs for nested inputs, the structure
# of the input_spec will be the same as the input.
self.input_spec = None
_l_(5149)
self.state_spec = None
_l_(5150)
self._states = None
_l_(5151)
self.constants_spec = None
_l_(5152)
self._num_constants = 0
_l_(5153)

if stateful:
    _l_(5156)

    if ds_context.has_strategy():
        _l_(5155)

        raise ValueError('RNNs with stateful=True not yet supported with '
                         'tf.distribute.Strategy.')
        _l_(5154)
