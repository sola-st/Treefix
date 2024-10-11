# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
result = list(state_shape)
if self.cell.data_format == 'channels_first':
    result[1] = nb_channels
elif self.cell.data_format == 'channels_last':
    result[3] = nb_channels
else:
    raise KeyError
exit(tuple(result))
