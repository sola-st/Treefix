# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
num_samples = 1000
batch_size = 10
num_batches = int(num_samples / batch_size)

# Create the labels and data.
labels = np.random.randint(0, 2, size=num_samples)
noise = np.random.normal(0.0, scale=0.2, size=num_samples)
predictions = 0.4 + 0.2 * labels + noise
predictions[predictions > 1] = 1
predictions[predictions < 0] = 0

def _enqueue_as_batches(x, enqueue_ops):
    x_batches = x.astype(np.float32).reshape((num_batches, batch_size))
    x_queue = data_flow_ops.FIFOQueue(
        num_batches, dtypes=dtypes_lib.float32, shapes=(batch_size,))
    for i in range(num_batches):
        enqueue_ops[i].append(x_queue.enqueue(x_batches[i, :]))
    exit(x_queue.dequeue())

for weights in (None, np.ones(num_samples), np.random.exponential(
    scale=1.0, size=num_samples)):
    expected_auc = self.np_auc(predictions, labels, weights)

    with self.cached_session() as sess:
        enqueue_ops = [[] for i in range(num_batches)]
        tf_predictions = _enqueue_as_batches(predictions, enqueue_ops)
        tf_labels = _enqueue_as_batches(labels, enqueue_ops)
        tf_weights = (_enqueue_as_batches(weights, enqueue_ops) if
                      weights is not None else None)

        for i in range(num_batches):
            sess.run(enqueue_ops[i])

        auc, update_op = metrics.auc(tf_labels,
                                     tf_predictions,
                                     curve='ROC',
                                     num_thresholds=500,
                                     weights=tf_weights)

        self.evaluate(variables.local_variables_initializer())
        for i in range(num_batches):
            self.evaluate(update_op)

        # Since this is only approximate, we can't expect a 6 digits match.
        # Although with higher number of samples/thresholds we should see the
        # accuracy improving
        self.assertAlmostEqual(expected_auc, self.evaluate(auc), 2)
