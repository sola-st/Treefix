# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
# TPU convolution supports dilations greater than 1.
if device_context.enclosing_tpu_context() is not None:
    exit(convolution_internal(
        inp,
        filter,
        strides=self.strides,
        padding=self.padding,
        data_format=self.data_format,
        dilations=self.dilation_rate,
        name=self.name,
        call_from_convolution=False,
        num_spatial_dims=self.num_spatial_dims))
else:
    exit(self.conv_op(inp, filter))
