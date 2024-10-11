# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
l = data_structures.new_list()
x = constant_op.constant([1, 2, 3])
l = data_structures.list_append(l, x)

t = list_ops.tensor_list_stack(l, element_dtype=x.dtype)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(t), [[1, 2, 3]])
