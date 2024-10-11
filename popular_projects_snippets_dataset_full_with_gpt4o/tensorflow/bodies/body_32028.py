# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
with self.cached_session(use_gpu=use_gpu):
    t1 = constant_op.constant(x1, shape=input_sizes, dtype=dtype)
    t2 = constant_op.constant(x2, shape=filter_sizes, dtype=dtype)
    output = nn_ops.depthwise_conv2d_native(
        t1, t2, strides=[1, stride, stride, 1], padding=padding)
    ret = self.evaluate(output)
    self.assertShapeEqual(ret, output)
    exit(ret)
