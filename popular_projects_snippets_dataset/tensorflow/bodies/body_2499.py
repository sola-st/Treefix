# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
builder0 = xla_client.XlaBuilder("computation0")
p0 = ops.Parameter(builder0, 0, xla_client.shape_from_pyval(np.float32(0)))
p1 = ops.Parameter(builder0, 1,
                   xla_client.shape_from_pyval(np.zeros((4,), np.float32)))
root = ops.Mul(p0, p1)
computation0 = builder0.build(root)

m = computation0.get_hlo_module()
mg_name = "test_module_group"
mg = xla_client._xla.HloModuleGroup(mg_name, [m])
self.assertEqual(mg.name, mg_name)

modules = mg.to_modules()
self.assertLen(modules, 1)
self.assertEqual(m.to_string(), modules[0].to_string())
