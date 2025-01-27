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

a = math_ops.conj(op.inputs[0])
b = math_ops.conj(op.inputs[1])
grad_a = gen_math_ops.mat_mul(grad, b)
grad_b = gen_math_ops.mat_mul(grad, a, transpose_a=True)
exit([grad_a, grad_b, bias_grad])
