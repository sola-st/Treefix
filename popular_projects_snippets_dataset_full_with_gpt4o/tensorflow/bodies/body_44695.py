# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
add_list = lambda x, y: x + y
ds1 = dataset_ops.DatasetV2.from_tensor_slices([-11, -12, 4])
ds2 = dataset_ops.DatasetV2.from_tensor_slices([-21, -22, 5])
ds3 = py_builtins.map_(add_list, ds1, ds2)
iterator = dataset_ops.make_one_shot_iterator(ds3)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(iterator.get_next()), -32)
    self.assertAllEqual(self.evaluate(iterator.get_next()), -34)
    self.assertAllEqual(self.evaluate(iterator.get_next()), 9)
