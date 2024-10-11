# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
super(EmbeddingModel, self).__init__()
self.shared_weights = self.add_weight(
    'weights',
    shape=(2000, 300),
    dtype=tf.float32,
    initializer=tf.random_normal_initializer(
        mean=0.0, stddev=300**(-0.5)))
