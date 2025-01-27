# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
super(Model, self).__init__()
# A None name will cause a failure in exporting to a saved model.
self.shared_weights = self.add_weight(
    name=None,
    shape=(20, 1),
    dtype=tf.float32,
    initializer=tf.random_normal_initializer(
        mean=0.0, stddev=300**(-0.5)))
