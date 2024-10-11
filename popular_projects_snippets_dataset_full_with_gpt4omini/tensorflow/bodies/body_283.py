# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
metrics = [
    "accuracy",
    "auc",
    "average_precision_at_k",
    "false_negatives",
    "false_negatives_at_thresholds",
    "false_positives",
    "false_positives_at_thresholds",
    "mean",
    "mean_absolute_error",
    "mean_cosine_distance",
    "mean_iou",
    "mean_per_class_accuracy",
    "mean_relative_error",
    "mean_squared_error",
    "mean_tensor",
    "percentage_below",
    "precision",
    "precision_at_k",
    "precision_at_thresholds",
    "precision_at_top_k",
    "recall",
    "recall_at_k",
    "recall_at_thresholds",
    "recall_at_top_k",
    "root_mean_squared_error",
    "sensitivity_at_specificity",
    "sparse_average_precision_at_k",
    "sparse_precision_at_k",
    "specificity_at_sensitivity",
    "true_negatives",
    "true_negatives_at_thresholds",
    "true_positives",
    "true_positives_at_thresholds",
]
for m in metrics:
    text = "tf.metrics." + m + "(a, b)"
    _, report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual("tf.compat.v1.metrics." + m + "(a, b)", new_text)
    self.assertIn(
        "tf.metrics have been replaced with object oriented versions", report)
