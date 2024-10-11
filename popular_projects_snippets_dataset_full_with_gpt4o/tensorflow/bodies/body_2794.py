# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_ops_test.py
self.skipTest('Fix tanh gradients')
input_ = tf.random.uniform([1, 4, 4, 1])
filter_ = tf.random.uniform([2, 2, 1, 8])
bias = tf.zeros([8])
kwargs = {
    'input_': input_,
    'filter_': filter_,
    'bias': bias,
    'stride_w': 2,
    'stride_h': 2,
    'dilation_w': 1,
    'dilation_h': 1,
    'padding': 'SAME',
    'act': 'TANH'
}

self._assertOpAndComposite([input_, filter_, bias],
                           tf.function(gen_mnist_ops.new_conv2d),
                           ops_defs._composite_conv_add_relu, kwargs)
