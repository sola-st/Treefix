# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
label_values = np.ones(shape=(2, 3))
prediction_values = np.zeros(shape=(2, 3, 1))
static_labels, static_predictions = (
    confusion_matrix.remove_squeezable_dimensions(
        label_values, prediction_values))

labels_placeholder = array_ops.placeholder(dtype=dtypes.int32)
predictions_placeholder = array_ops.placeholder(dtype=dtypes.int32)
dynamic_labels, dynamic_predictions = (
    confusion_matrix.remove_squeezable_dimensions(
        labels_placeholder, predictions_placeholder))

expected_prediction_values = np.reshape(prediction_values, newshape=(2, 3))
with self.cached_session():
    self.assertAllEqual(label_values, self.evaluate(static_labels))
    self.assertAllEqual(expected_prediction_values,
                        self.evaluate(static_predictions))
    feed_dict = {
        labels_placeholder: label_values,
        predictions_placeholder: prediction_values
    }
    self.assertAllEqual(
        label_values, dynamic_labels.eval(feed_dict=feed_dict))
    self.assertAllEqual(
        expected_prediction_values,
        dynamic_predictions.eval(feed_dict=feed_dict))
