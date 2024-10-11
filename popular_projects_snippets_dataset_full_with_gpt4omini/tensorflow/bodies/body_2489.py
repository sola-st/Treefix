# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
builder = xla_client.XlaBuilder("acomputation")
p0 = ops.Parameter(builder, 0, xla_client.shape_from_pyval(np.float32(0)))
p1 = ops.Parameter(builder, 1,
                   xla_client.shape_from_pyval(np.zeros((4,), np.float32)))
x = ops.Mul(p0, p1)
ops.Add(x, x)
exit(builder.build())
