# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = """
def _log_prob(self, x):
  return tf.reduce_logsumexp(
      (self.mixture_distribution.logits + self.distribution.log_prob(
          x[..., tf.newaxis])),
          axis=-1)"""
expected_text = """
def _log_prob(self, x):
  return tf.reduce_logsumexp(
      input_tensor=(self.mixture_distribution.logits + self.distribution.log_prob(
          x[..., tf.newaxis])),
          axis=-1)"""
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
