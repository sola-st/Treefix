# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = data_structures.tf_tensor_array_new([3, 4, 5])
t = l.stack()
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(t), [3, 4, 5])
