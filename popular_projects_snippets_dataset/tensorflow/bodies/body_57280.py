# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/acceleration/mini_benchmark/metrics/blazeface_metrics.py
"""Calculate metrics from expected and actual blazeface outputs.

  Args:
    expected_box_encodings: box encodings from model
    expected_scores: classifications from model
    actual_box_encodings: golden box encodings
    actual_scores: golden classifications

  Returns:
    two-item list with classification error and localization error
  """
squashed_expected_scores = tf.math.divide(1.0,
                                          1.0 + tf.math.exp(-expected_scores))
squashed_actual_scores = tf.math.divide(1.0,
                                        1.0 + tf.math.exp(-actual_scores))
kld_metric = kl_divergence.symmetric_kl_divergence(expected_scores,
                                                   actual_scores)
# ML Kit uses 0.5 as the threshold. We use
# 0.1 to use more possible boxes based on experimentation with the model.
high_scoring_indices = tf.math.logical_or(
    tf.math.greater(squashed_expected_scores, 0.1),
    tf.math.greater(squashed_actual_scores, 0.1))

high_scoring_actual_boxes = tf.where(
    condition=tf.broadcast_to(
        input=high_scoring_indices, shape=tf.shape(actual_box_encodings)),
    x=actual_box_encodings,
    y=expected_box_encodings)
box_diff = high_scoring_actual_boxes - expected_box_encodings
box_squared_diff = tf.math.pow(box_diff, 2)
# MSE is calculated over the high-scoring boxes.
box_mse = tf.divide(
    tf.math.reduce_sum(box_squared_diff),
    tf.math.maximum(
        tf.math.count_nonzero(high_scoring_indices, dtype=tf.float32), 1.0))
# Thresholds were determined experimentally by running validation on a variety
# of devices. Known good devices give KLD ~10-e7 and MSE ~10-e12. A buggy
# NNAPI implementation gives KLD > 200 and MSE > 100.
ok = tf.logical_and(kld_metric < 0.1, box_mse < 0.01)

exit([kld_metric, box_mse, ok])
