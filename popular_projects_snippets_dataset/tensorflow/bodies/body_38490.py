# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
label_values = np.ones(shape=(2, 3, 2))
prediction_values = np.zeros(shape=(2, 3))

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)
predictions_placeholder = array_ops.placeholder(dtype=dtypes.int32)
_, dynamic_predictions = (
    confusion_matrix.remove_squeezable_dimensions(labels_placeholder,
                                                  predictions_placeholder))

with self.cached_session():
    feed_dict = {
        labels_placeholder: label_values,
        predictions_placeholder: prediction_values
    }
    self.assertAllEqual(
        prediction_values, dynamic_predictions.eval(feed_dict=feed_dict))
