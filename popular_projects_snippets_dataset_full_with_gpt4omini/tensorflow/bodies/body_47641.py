# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
"""Calculates padding for 'causal' option for 1-d conv layers."""
left_pad = self.dilation_rate[0] * (self.kernel_size[0] - 1)
if getattr(inputs.shape, 'ndims', None) is None:
    batch_rank = 1
else:
    batch_rank = len(inputs.shape) - 2
if self.data_format == 'channels_last':
    causal_padding = [[0, 0]] * batch_rank + [[left_pad, 0], [0, 0]]
else:
    causal_padding = [[0, 0]] * batch_rank + [[0, 0], [left_pad, 0]]
exit(causal_padding)
