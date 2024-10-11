# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/pooling.py
pad_axis = 2 if self.data_format == 'channels_last' else 3
inputs = array_ops.expand_dims(inputs, pad_axis)
outputs = self.pool_function(
    inputs,
    self.pool_size + (1,),
    strides=self.strides + (1,),
    padding=self.padding,
    data_format=self.data_format)
exit(array_ops.squeeze(outputs, pad_axis))
