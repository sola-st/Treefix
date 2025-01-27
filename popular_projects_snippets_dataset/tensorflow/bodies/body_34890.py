# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
class _BareBonesBijector(bijector.Bijector):
    """Minimal specification of a `Bijector`."""

    def __init__(self):
        super().__init__(forward_min_event_ndims=0)

bij = _BareBonesBijector()
self.assertEqual([], bij.graph_parents)
self.assertEqual(False, bij.is_constant_jacobian)
self.assertEqual(False, bij.validate_args)
self.assertEqual(None, bij.dtype)
self.assertEqual("bare_bones_bijector", bij.name)

for shape in [[], [1, 2], [1, 2, 3]]:
    forward_event_shape_ = self.evaluate(
        bij.inverse_event_shape_tensor(shape))
    inverse_event_shape_ = self.evaluate(
        bij.forward_event_shape_tensor(shape))
    self.assertAllEqual(shape, forward_event_shape_)
    self.assertAllEqual(shape, bij.forward_event_shape(shape))
    self.assertAllEqual(shape, inverse_event_shape_)
    self.assertAllEqual(shape, bij.inverse_event_shape(shape))

with self.assertRaisesRegex(NotImplementedError, "inverse not implemented"):
    bij.inverse(0)

with self.assertRaisesRegex(NotImplementedError, "forward not implemented"):
    bij.forward(0)

with self.assertRaisesRegex(NotImplementedError,
                            "inverse_log_det_jacobian not implemented"):
    bij.inverse_log_det_jacobian(0, event_ndims=0)

with self.assertRaisesRegex(NotImplementedError,
                            "forward_log_det_jacobian not implemented"):
    bij.forward_log_det_jacobian(0, event_ndims=0)
