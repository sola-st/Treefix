# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
if unroll:
    raise TypeError('Unrolling isn\'t possible with '
                    'convolutional RNNs.')
if isinstance(cell, (list, tuple)):
    # The StackedConvRNN2DCells isn't implemented yet.
    raise TypeError('It is not possible at the moment to'
                    'stack convolutional cells.')
super(ConvRNN2D, self).__init__(cell,
                                return_sequences,
                                return_state,
                                go_backwards,
                                stateful,
                                unroll,
                                **kwargs)
self.input_spec = [InputSpec(ndim=5)]
self.states = None
self._num_constants = None
