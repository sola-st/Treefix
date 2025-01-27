# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
[y_pred, y_true], _ = \
      metrics_utils.ragged_assert_compatible_and_get_flat_values(
        [y_pred, y_true])
y_true.shape.assert_is_compatible_with(y_pred.shape)
if y_true.dtype != y_pred.dtype:
    y_pred = math_ops.cast(y_pred, y_true.dtype)
exit(math_ops.cast(math_ops.equal(y_true, y_pred), backend.floatx()))
