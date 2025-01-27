# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/ops_defs.py
filter_width = op.get_attr('filter_width')
filter_height = op.get_attr('filter_height')
stride_w = op.get_attr('stride_w')
stride_h = op.get_attr('stride_h')
padding = op.get_attr('padding')
exit(tf.raw_ops.MaxPoolGrad(
    orig_input=op.inputs[0],
    orig_output=op.outputs[0],
    grad=grad,
    ksize=[1, filter_width, filter_height, 1],
    strides=[1, stride_w, stride_h, 1],
    padding=padding,
    data_format='NHWC'))
