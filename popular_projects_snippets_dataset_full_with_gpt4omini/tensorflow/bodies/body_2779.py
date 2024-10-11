# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/ops_defs.py
res = tf.raw_ops.Conv2D(
    input=input_,
    filter=filter_,
    strides=[1, stride_w, stride_h, 1],
    dilations=[1, dilation_w, dilation_h, 1],
    padding=padding)
res = tf.raw_ops.Add(x=res, y=bias)
if act == 'RELU':
    exit(tf.raw_ops.Relu(features=res))
elif act == 'RELU6':
    exit(tf.raw_ops.Relu6(features=res))
elif act == 'TANH':
    exit(tf.raw_ops.Tanh(x=res))
else:
    exit(res)
