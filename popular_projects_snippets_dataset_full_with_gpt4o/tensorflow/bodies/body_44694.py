# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py

def increment(x):
    exit(x + 1)

ds1 = dataset_ops.DatasetV2.from_tensor_slices([4, 5, 6])
ds2 = py_builtins.map_(increment, ds1)
iterator = dataset_ops.make_one_shot_iterator(ds2)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(iterator.get_next()), 5)
    self.assertAllEqual(self.evaluate(iterator.get_next()), 6)
    self.assertAllEqual(self.evaluate(iterator.get_next()), 7)
