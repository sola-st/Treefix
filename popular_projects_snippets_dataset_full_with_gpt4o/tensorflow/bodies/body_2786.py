# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/mnist_train.py
self.weights = {
    'f1':
        tf.Variable(
            tf.random.truncated_normal([5, 5, num_channels, n_hidden_1],
                                       stddev=0.1,
                                       seed=seed)),
    'f2':
        tf.Variable(
            tf.random.truncated_normal([5, 5, n_hidden_1, n_hidden_2],
                                       stddev=0.1,
                                       seed=seed)),
    'f3':
        tf.Variable(
            tf.random.truncated_normal([n_hidden_3, flatten_size],
                                       stddev=0.1,
                                       seed=seed)),
    'f4':
        tf.Variable(
            tf.random.truncated_normal([num_classes, n_hidden_3],
                                       stddev=0.1,
                                       seed=seed)),
}

self.biases = {
    'b1': tf.Variable(tf.zeros([n_hidden_1])),
    'b2': tf.Variable(tf.zeros([n_hidden_2])),
    'b3': tf.Variable(tf.zeros([n_hidden_3])),
    'b4': tf.Variable(tf.zeros([num_classes])),
}
