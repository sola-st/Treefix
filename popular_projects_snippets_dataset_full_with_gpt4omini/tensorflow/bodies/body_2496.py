# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
c = xla_client.XlaBuilder(self.id())
p1 = ops.Parameter(
    c, 0,
    xla_client.shape_from_pyval(np.array(
        1.0, np.float32)).with_major_to_minor_layout_if_absent())
p2 = ops.Parameter(
    c, 1,
    xla_client.shape_from_pyval(np.array(
        1.0, np.float32)).with_major_to_minor_layout_if_absent())
out = ops.Add(p1, p2)
c.setup_alias([], 0, [])
c.build(out)
