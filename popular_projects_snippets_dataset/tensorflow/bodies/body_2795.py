# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_ops_test.py
input_ = tf.random.uniform([2, 4])
filter_ = tf.random.uniform([3, 4])
bias = tf.zeros([3])
kwargs = {'input_': input_, 'filter_': filter_, 'bias': bias, 'act': 'RELU'}

self._assertOpAndComposite([input_, filter_, bias],
                           tf.function(gen_mnist_ops.new_fully_connected),
                           ops_defs._composite_fully_connected, kwargs)
