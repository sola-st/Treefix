# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
t = tf.math.add(self.v1, self.v2)
exit(tf.math.add(t, self.table.lookup(x)))
