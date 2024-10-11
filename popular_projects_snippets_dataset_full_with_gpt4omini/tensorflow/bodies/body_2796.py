# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_ops_test.py
input_ = tf.random.uniform([8, 4, 4, 1])
kwargs = {
    'input_': input_,
    'stride_w': 2,
    'stride_h': 2,
    'filter_width': 1,
    'filter_height': 1,
    'padding': 'SAME',
}

self._assertOpAndComposite([input_],
                           tf.function(gen_mnist_ops.new_max_pool),
                           ops_defs._composite_max_pool, kwargs)
