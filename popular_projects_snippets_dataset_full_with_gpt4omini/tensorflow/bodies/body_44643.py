# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = data_structures.new_list()
# Can't evaluate an empty list.
# TODO(mdan): sess.run should allow tf.variant maybe?
self.assertTrue(isinstance(l, ops.Tensor))
