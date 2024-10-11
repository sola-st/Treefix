# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
losses = [
    "absolute_difference",
    "add_loss",
    "compute_weighted_loss",
    "cosine_distance",
    "get_losses",
    "get_regularization_loss",
    "get_regularization_losses",
    "get_total_loss",
    "hinge_loss",
    "huber_loss",
    "log_loss",
    "mean_pairwise_squared_error",
    "mean_squared_error",
    "sigmoid_cross_entropy",
    "softmax_cross_entropy",
    "sparse_softmax_cross_entropy",
]
for l in losses:
    text = "tf.losses." + l + "(a, b)"
    _, report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual("tf.compat.v1.losses." + l + "(a, b)", new_text)
    self.assertIn(
        "tf.losses have been replaced with object oriented versions", report)
