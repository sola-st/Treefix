# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = ops.convert_to_tensor([1, 1, 1])  # shape 3,
labels = array_ops.expand_dims(ops.convert_to_tensor([1, 0, 0]),
                               1)  # shape 3, 1

weights = [[100], [1], [1]]  # shape 3, 1
weights_placeholder = array_ops.placeholder(
    dtype=dtypes_lib.int32, name='weights')
feed_dict = {weights_placeholder: weights}

with self.cached_session():
    accuracy, update_op = metrics.accuracy(labels, predictions,
                                           weights_placeholder)

    self.evaluate(variables.local_variables_initializer())
    # if streaming_accuracy does not flatten the weight, accuracy would be
    # 0.33333334 due to an intended broadcast of weight. Due to flattening,
    # it will be higher than .95
    self.assertGreater(update_op.eval(feed_dict=feed_dict), .95)
    self.assertGreater(accuracy.eval(feed_dict=feed_dict), .95)
