# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
self.v = tf.Variable(
    0.,
    synchronization=tf.VariableSynchronization.ON_WRITE,
    aggregation=tf.VariableAggregation.MEAN)
