# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
num_samples = 1000
batch_size = 10
num_batches = int(num_samples / batch_size)

# Create the labels and data.
labels = np.random.randint(0, 2, size=(num_samples, 1))
noise = np.random.normal(0.0, scale=0.2, size=(num_samples, 1))
predictions = 0.4 + 0.2 * labels + noise
predictions[predictions > 1] = 1
predictions[predictions < 0] = 0
thresholds = [0.3]

tp = 0
fp = 0
fn = 0
tn = 0
for i in range(num_samples):
    if predictions[i] > thresholds[0]:
        if labels[i] == 1:
            tp += 1
        else:
            fp += 1
    else:
        if labels[i] == 1:
            fn += 1
        else:
            tn += 1
epsilon = 1e-7
expected_prec = tp / (epsilon + tp + fp)
expected_rec = tp / (epsilon + tp + fn)

labels = labels.astype(np.float32)
predictions = predictions.astype(np.float32)

with self.cached_session() as sess:
    # Reshape the data so its easy to queue up:
    predictions_batches = predictions.reshape((batch_size, num_batches))
    labels_batches = labels.reshape((batch_size, num_batches))

    # Enqueue the data:
    predictions_queue = data_flow_ops.FIFOQueue(
        num_batches, dtypes=dtypes_lib.float32, shapes=(batch_size,))
    labels_queue = data_flow_ops.FIFOQueue(
        num_batches, dtypes=dtypes_lib.float32, shapes=(batch_size,))

    for i in range(int(num_batches)):
        tf_prediction = constant_op.constant(predictions_batches[:, i])
        tf_label = constant_op.constant(labels_batches[:, i])
        sess.run([
            predictions_queue.enqueue(tf_prediction),
            labels_queue.enqueue(tf_label)
        ])

    tf_predictions = predictions_queue.dequeue()
    tf_labels = labels_queue.dequeue()

    prec, prec_op = metrics.precision_at_thresholds(tf_labels, tf_predictions,
                                                    thresholds)
    rec, rec_op = metrics.recall_at_thresholds(tf_labels, tf_predictions,
                                               thresholds)

    self.evaluate(variables.local_variables_initializer())
    for _ in range(int(num_samples / batch_size)):
        self.evaluate([prec_op, rec_op])
    # Since this is only approximate, we can't expect a 6 digits match.
    # Although with higher number of samples/thresholds we should see the
    # accuracy improving
    self.assertAlmostEqual(expected_prec, self.evaluate(prec), 2)
    self.assertAlmostEqual(expected_rec, self.evaluate(rec), 2)
