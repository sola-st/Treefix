# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
x = array_ops.placeholder(
    dtype=dtypes.float32, shape=[1, 4, 4, 3], name='input')
f = constant_op.constant([0.5],
                         dtype=dtypes.float32,
                         shape=[2, 2, 3, 2],
                         name='filter')
strides = [1, 1, 1, 1]
padding = 'SAME'
out = nn_impl.depthwise_conv2d(x, f, strides, padding)

grad_wrt_input = gradients_impl.gradients(out, x)[0]
self.run_test(f, grad_wrt_input)

grad_wrt_filter = gradients_impl.gradients(out, f)[0]
self.run_test(x, grad_wrt_filter)
