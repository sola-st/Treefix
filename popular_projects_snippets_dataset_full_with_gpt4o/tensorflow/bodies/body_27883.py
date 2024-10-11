# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
dataset = dataset_ops.Dataset.from_tensors(components)
dataset = dataset.map(lambda x, y, z: ((x, z), (y[0], y[1])))

dataset = dataset.flat_map(
    lambda x, y: dataset_ops.Dataset.from_tensors(
        ((x[0], x[1]), (y[0], y[1])))).batch(32)

get_next = self.getNext(dataset)
(w, x), (y, z) = get_next()
self.assertEqual(dtypes.int64, w.dtype)
self.assertEqual(dtypes.int64, x.dtype)
self.assertEqual(dtypes.float64, y.dtype)
self.assertEqual(dtypes.float64, z.dtype)
self.assertEqual(expected_shapes, [
    w.shape.as_list(),
    x.shape.as_list(),
    y.shape.as_list(),
    z.shape.as_list()
])

get_next = self.getNext(dataset)
(w, x), (y, z) = get_next()
self.assertEqual(dtypes.int64, w.dtype)
self.assertEqual(dtypes.int64, x.dtype)
self.assertEqual(dtypes.float64, y.dtype)
self.assertEqual(dtypes.float64, z.dtype)
self.assertEqual(expected_shapes, [
    w.shape.as_list(),
    x.shape.as_list(),
    y.shape.as_list(),
    z.shape.as_list()
])
