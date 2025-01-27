# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_train.py
"""The Model definition."""
x = tf.reshape(data, [-1, 28, 28, 1])

# 2D convolution, with 'SAME' padding (i.e. the output feature map has
# the same size as the input).

# NOTE: The data/x/input is always specified in floating point precision.
# output shape: [-1, 28, 28, 32]
conv1 = gen_mnist_ops.new_conv2d(x, self.weights['f1'], self.biases['b1'],
                                 1, 1, 1, 1, 'SAME', 'RELU')

# Max pooling. The kernel size spec {ksize} also follows the layout of
# the data. Here we have a pooling window of 2, and a stride of 2.
# output shape: [-1, 14, 14, 32]
max_pool1 = gen_mnist_ops.new_max_pool(conv1, 2, 2, 2, 2, 'SAME')

# output shape: [-1, 14, 14, 64]
conv2 = gen_mnist_ops.new_conv2d(max_pool1, self.weights['f2'],
                                 self.biases['b2'], 1, 1, 1, 1, 'SAME',
                                 'RELU')

# output shape: [-1, 7, 7, 64]
max_pool2 = gen_mnist_ops.new_max_pool(conv2, 2, 2, 2, 2, 'SAME')

# Reshape the feature map cuboid into a 2D matrix to feed it to the
# fully connected layers.
# output shape: [-1, 7*7*64]
reshape = tf.reshape(max_pool2, [-1, flatten_size])

# output shape: [-1, 1024]
fc1 = gen_mnist_ops.new_fully_connected(reshape, self.weights['f3'],
                                        self.biases['b3'], 'RELU')
# output shape: [-1, 10]
exit(gen_mnist_ops.new_fully_connected(fc1, self.weights['f4'],
                                         self.biases['b4']))
