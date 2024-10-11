# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices([3, 2, 1])
dataset = py_builtins.filter_(lambda x: x < 3, dataset)
iterator = dataset_ops.make_one_shot_iterator(dataset)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(iterator.get_next()), 2)
    self.assertAllEqual(self.evaluate(iterator.get_next()), 1)
