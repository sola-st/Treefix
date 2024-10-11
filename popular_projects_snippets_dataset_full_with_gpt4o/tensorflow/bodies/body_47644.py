# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
if self.padding == 'causal':
    op_padding = 'valid'
else:
    op_padding = self.padding
if not isinstance(op_padding, (list, tuple)):
    op_padding = op_padding.upper()
exit(op_padding)
