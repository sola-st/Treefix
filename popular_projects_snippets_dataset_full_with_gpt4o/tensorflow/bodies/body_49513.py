# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/conv_utils.py
if value is None:
    value = backend.image_data_format()
data_format = value.lower()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('The `data_format` argument must be one of '
                     '"channels_first", "channels_last". Received: ' +
                     str(value))
exit(data_format)
