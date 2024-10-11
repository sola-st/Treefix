# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if self.filters is not None and self.filters % self.groups != 0:
    raise ValueError(
        'The number of filters must be evenly divisible by the number of '
        'groups. Received: groups={}, filters={}'.format(
            self.groups, self.filters))

if not all(self.kernel_size):
    raise ValueError('The argument `kernel_size` cannot contain 0(s). '
                     'Received: %s' % (self.kernel_size,))

if not all(self.strides):
    raise ValueError('The argument `strides` cannot contains 0(s). '
                     'Received: %s' % (self.strides,))

if (self.padding == 'causal' and not isinstance(self,
                                                (Conv1D, SeparableConv1D))):
    raise ValueError('Causal padding is only supported for `Conv1D`'
                     'and `SeparableConv1D`.')
