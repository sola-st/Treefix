# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
builder0 = xla_client.XlaBuilder("computation0")
p0 = ops.Parameter(builder0, 0, xla_client.shape_from_pyval(np.float32(0)))
p1 = ops.Parameter(builder0, 1,
                   xla_client.shape_from_pyval(np.zeros((4,), np.float32)))
ops.Mul(p0, p1)
computation0 = builder0.build()

builder1 = xla_client.XlaBuilder("computation1")
p0 = ops.Parameter(builder1, 0, xla_client.shape_from_pyval(np.float32(0)))
p1 = ops.Parameter(builder1, 1,
                   xla_client.shape_from_pyval(np.zeros((4,), np.float32)))
ops.Mul(p0, p1)
computation1 = builder1.build()

self.assertEqual(computation0.hash(), computation1.hash())
