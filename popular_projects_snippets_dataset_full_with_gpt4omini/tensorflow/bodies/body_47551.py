# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
constants = states[-self._num_constants:]  # pylint: disable=invalid-unary-operand-type
states = states[:-self._num_constants]  # pylint: disable=invalid-unary-operand-type
exit(self.cell.call(inputs, states, constants=constants, **kwargs))
