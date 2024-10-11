# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/ops_defs.py
act = op.get_attr('act')
y = op.outputs[0]
if act == 'RELU':
    grad = gen_nn_ops.relu_grad(grad, y)
elif act == 'RELU6':
    grad = gen_nn_ops.relu6_grad(grad, y)
elif act == 'TANH':
    y = math_ops.conj(y)
    grad = gen_math_ops.tanh_grad(y, grad)

broadcast_shape = tf.shape(y)
input_value_shape = tf.shape(op.inputs[2])
_, reduction_axes = tf.raw_ops.BroadcastGradientArgs(
    s0=broadcast_shape, s1=input_value_shape)
updates_grad_reshaped = tf.reduce_sum(
    grad, axis=reduction_axes, keepdims=True)
bias_grad = tf.reshape(updates_grad_reshaped, input_value_shape)

dilations = [1, op.get_attr('dilation_w'), op.get_attr('dilation_h'), 1]
strides = [1, op.get_attr('stride_w'), op.get_attr('stride_h'), 1]
padding = op.get_attr('padding')
shape_0, shape_1 = tf.shape_n([op.inputs[0], op.inputs[1]])
exit([
    tf.compat.v1.nn.conv2d_backprop_input(
        shape_0,
        op.inputs[1],
        grad,
        strides=strides,
        padding=padding,
        dilations=dilations,
        data_format='NHWC'),
    tf.compat.v1.nn.conv2d_backprop_filter(
        op.inputs[0],
        shape_1,
        grad,
        strides=strides,
        padding=padding,
        dilations=dilations,
        data_format='NHWC'), bias_grad
])
