# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset_1 = dataset_ops.DatasetV2.from_tensor_slices([-1, 2, 3])
dataset_2 = dataset_ops.DatasetV2.from_tensor_slices([1, -2, 3])
dataset_3 = dataset_ops.DatasetV2.from_tensor_slices([-1, -2, -3])
dataset_4 = dataset_ops.DatasetV2.zip((dataset_1, dataset_2))
dataset = dataset_ops.DatasetV2.zip((dataset_3, dataset_4))
dataset = py_builtins.abs_(dataset)
iterator = dataset_ops.make_one_shot_iterator(dataset)
with self.cached_session() as sess:
    for i in range(1, 4):
        actual = self.evaluate(iterator.get_next())
        self.assertAllEqual(actual[0], i)
        self.assertAllEqual(actual[1], (i, i))
