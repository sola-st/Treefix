# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
ds1 = dataset_ops.DatasetV2.from_tensor_slices([-11, -12, 4])
ds2 = dataset_ops.DatasetV2.from_tensor_slices([-21, -22, 5])
ds3 = py_builtins.zip_(ds1, ds2)
iterator = dataset_ops.make_one_shot_iterator(ds3)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(iterator.get_next()), (-11, -21))
    self.assertAllEqual(self.evaluate(iterator.get_next()), (-12, -22))
    self.assertAllEqual(self.evaluate(iterator.get_next()), (4, 5))
