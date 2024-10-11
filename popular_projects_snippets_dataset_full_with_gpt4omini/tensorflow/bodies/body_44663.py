# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices([-1, 2, 3])
dataset = py_builtins.abs_(dataset)
iterator = dataset_ops.make_one_shot_iterator(dataset)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(iterator.get_next()), 1)
    self.assertAllEqual(self.evaluate(iterator.get_next()), 2)
    self.assertAllEqual(self.evaluate(iterator.get_next()), 3)
