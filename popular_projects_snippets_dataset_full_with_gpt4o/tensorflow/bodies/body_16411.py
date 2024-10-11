# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
exit(_NonAtrousConvolution(
    self.input_shape,
    filter_shape=self.filter_shape,
    padding=padding,
    data_format=self.data_format,
    strides=self.strides,
    name=self.name,
    num_batch_dims=self.num_batch_dims))
