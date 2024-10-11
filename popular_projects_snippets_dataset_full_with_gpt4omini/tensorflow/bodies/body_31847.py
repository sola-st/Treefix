# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
super(LogLossTest, self).setUp()
predictions = np.asarray([.9, .2, .2, .8, .4, .6]).reshape((2, 3))
labels = np.asarray([1.0, 0.0, 1.0, 1.0, 0.0, 0.0]).reshape((2, 3))

self._np_predictions = predictions
self._np_labels = labels

epsilon = 1e-7
self._expected_losses = np.multiply(
    labels, np.log(predictions + epsilon)) + np.multiply(
        1 - labels, np.log(1 - predictions + epsilon))

self._predictions = constant_op.constant(predictions)
self._labels = constant_op.constant(labels)
