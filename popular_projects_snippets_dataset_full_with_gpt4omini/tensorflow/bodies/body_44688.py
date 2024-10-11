# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices(['a', 'c'])
start = constant_op.constant(20, dtype=dtypes.int64)
dataset = py_builtins.enumerate_(dataset, start)
iterator = dataset_ops.make_one_shot_iterator(dataset)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(iterator.get_next()), (20, b'a'))
    self.assertAllEqual(self.evaluate(iterator.get_next()), (21, b'c'))
