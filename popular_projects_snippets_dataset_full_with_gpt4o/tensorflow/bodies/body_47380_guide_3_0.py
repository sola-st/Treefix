kwargs = {'some_key': 'some_value'} # pragma: no cover
return_sequences = False # pragma: no cover
return_state = False # pragma: no cover
go_backwards = False # pragma: no cover
stateful = True # pragma: no cover
unroll = False # pragma: no cover
time_major = False # pragma: no cover
ds_context = type('MockContext', (object,), {'has_strategy': staticmethod(lambda: True)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
from l3.Runtime import _l_
if isinstance(cell, (list, tuple)):
    _l_(16902)

    cell = StackedRNNCells(cell)
    _l_(16901)
if not 'call' in dir(cell):
    _l_(16904)

    raise ValueError('`cell` should have a `call` method. '
                     'The RNN was passed:', cell)
    _l_(16903)
if not 'state_size' in dir(cell):
    _l_(16906)

    raise ValueError('The RNN cell should have '
                     'an attribute `state_size` '
                     '(tuple of integers, '
                     'one integer per RNN state).')
    _l_(16905)
# If True, the output for masked timestep will be zeros, whereas in the
# False case, output from previous timestep is returned for masked timestep.
self.zero_output_for_mask = kwargs.pop('zero_output_for_mask', False)
_l_(16907)

if 'input_shape' not in kwargs and (
    'input_dim' in kwargs or 'input_length' in kwargs):
    _l_(16910)

    input_shape = (kwargs.pop('input_length', None),
                   kwargs.pop('input_dim', None))
    _l_(16908)
    kwargs['input_shape'] = input_shape
    _l_(16909)

super(RNN, self).__init__(**kwargs)
_l_(16911)
self.cell = cell
_l_(16912)
self.return_sequences = return_sequences
_l_(16913)
self.return_state = return_state
_l_(16914)
self.go_backwards = go_backwards
_l_(16915)
self.stateful = stateful
_l_(16916)
self.unroll = unroll
_l_(16917)
self.time_major = time_major
_l_(16918)

self.supports_masking = True
_l_(16919)
# The input shape is unknown yet, it could have nested tensor inputs, and
# the input spec will be the list of specs for nested inputs, the structure
# of the input_spec will be the same as the input.
self.input_spec = None
_l_(16920)
self.state_spec = None
_l_(16921)
self._states = None
_l_(16922)
self.constants_spec = None
_l_(16923)
self._num_constants = 0
_l_(16924)

if stateful:
    _l_(16927)

    if ds_context.has_strategy():
        _l_(16926)

        raise ValueError('RNNs with stateful=True not yet supported with '
                         'tf.distribute.Strategy.')
        _l_(16925)
