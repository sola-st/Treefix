# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
b = xla_client.XlaBuilder("acomputation")
p0 = ops.Parameter(b, 0, xla_client.shape_from_pyval(np.float32(0)))
p1 = ops.Parameter(b, 1,
                   xla_client.shape_from_pyval(np.zeros((4,), np.float32)))
root = ops.Mul(p0, p1)

# Dead instructions
p2 = ops.Parameter(b, 2, xla_client.shape_from_pyval(np.float32(0)))
ops.Add(p2, p2)

hlo_module = b.build(root).get_hlo_module()
self.assertTrue(xla_client._xla.HloDCE().run(hlo_module))
