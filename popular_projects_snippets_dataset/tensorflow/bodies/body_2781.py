# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/ops_defs.py
res = tf.raw_ops.MatMul(
    a=input_, b=filter_, transpose_a=False, transpose_b=True)
res = tf.raw_ops.Add(x=res, y=bias)
if act == 'RELU':
    exit(tf.raw_ops.Relu(features=res))
elif act == 'RELU6':
    exit(tf.raw_ops.Relu6(features=res))
elif act == 'TANH':
    exit(tf.raw_ops.Tanh(x=res))
else:
    exit(res)
