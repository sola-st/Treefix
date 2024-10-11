# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with ops.device('CPU:0'):
    v = variables.Variable(1.)
empty_handle = array_ops.gather(
    v.handle[array_ops.newaxis], array_ops.zeros([0], dtype=dtypes.int32))
self.assertEqual(
    [0],
    empty_handle.shape.as_list())
