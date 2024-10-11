# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
a = array_ops.placeholder(np.float32, shape=(2, 3, 4))
upd = array_ops.placeholder(np.float32, shape=(1, 2, 3))
start_indices = array_ops.placeholder(np.int32, shape=(3,))

res = xla.dynamic_update_slice(a, upd, start_indices)
self.assertEqual(res.shape.as_list(), [2, 3, 4])

a = array_ops.placeholder(np.float32, shape=(None, 3, None))
res = xla.dynamic_update_slice(a, upd, start_indices)
self.assertEqual(res.shape.as_list(), [None, 3, None])
