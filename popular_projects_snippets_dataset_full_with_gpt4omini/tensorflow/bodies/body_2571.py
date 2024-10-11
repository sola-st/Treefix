# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform != "cpu":
    self.skipTest("Test requires cpu platform")
c = self._NewComputation()
for name, fn in custom_call_for_test.cpu_custom_call_targets.items():
    xla_client.register_custom_call_target(name, fn, platform="cpu")

opaque_str = b"foo"
ops.CustomCallWithLayout(
    c,
    b"test_add_input_and_opaque_len",
    operands=[
        ops.Constant(c, np.float32(1.25)),
        ops.Constant(c, np.float32(0.5))
    ],
    shape_with_layout=xla_client.Shape.array_shape(
        np.dtype(np.float32), (), ()),
    operand_shapes_with_layout=[
        xla_client.Shape.array_shape(np.dtype(np.float32), (), ()),
        xla_client.Shape.array_shape(np.dtype(np.float32), (), ()),
    ],
    # With opaque length = 3.0
    opaque=opaque_str,
    api_version=xla_client.ops.CustomCallApiVersion
    .API_VERSION_STATUS_RETURNING_UNIFIED)
self._ExecuteAndCompareClose(c, expected=[1.25 + len(opaque_str)])
