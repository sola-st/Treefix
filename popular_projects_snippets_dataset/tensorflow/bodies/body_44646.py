# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = data_structures.tf_tensor_list_new([],
                                       element_dtype=dtypes.int32,
                                       element_shape=())
t = list_ops.tensor_list_stack(l, element_dtype=dtypes.int32)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(t), [])
