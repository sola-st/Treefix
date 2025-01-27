# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for decay in ["tf.train.exponential_decay",
              "tf.train.polynomial_decay", "tf.train.natural_exp_decay",
              "tf.train.inverse_time_decay", "tf.train.cosine_decay",
              "tf.train.cosine_decay_restarts",
              "tf.train.linear_cosine_decay",
              "tf.train.noisy_linear_cosine_decay",
              "tf.train.piecewise_constant_decay",
             ]:

    text = "%s(a, b)\n" % decay
    _, report, unused_errors, _ = self._upgrade(text)
    self.assertIn("switch to the schedules in "
                  "`tf.keras.optimizers.schedules`", report)
