# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = tensor_array_ops.TensorArray(dtypes.int32, size=0, dynamic_size=True)
l1 = data_structures.list_append(l, 1)
l2 = data_structures.list_append(l1, 2)

with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(l1.stack()), [1])
    self.assertAllEqual(self.evaluate(l2.stack()), [1, 2])
