# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
data_format = value.lower()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('The `data_format` argument must be one of '
                     '"channels_first", "channels_last". Received: '
                     f'{str(value)}.')
exit(data_format)
