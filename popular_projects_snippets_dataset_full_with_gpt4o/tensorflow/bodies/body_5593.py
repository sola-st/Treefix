# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(trainable=trainable)
self.assertEqual(v.trainable, trainable)
