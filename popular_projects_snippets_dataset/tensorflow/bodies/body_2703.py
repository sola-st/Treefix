# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
to_infeed = NumpyArrayS32([1, 2, 3, 4])
c = self._NewComputation()
ops.GetTupleElement(
    ops.InfeedWithToken(
        ops.CreateToken(c),
        xla_client.shape_from_pyval(
            to_infeed[0]).with_major_to_minor_layout_if_absent()), 0)
compiled_c = self.backend.compile(c.build())
device = self.backend.local_devices()[0]
for item in to_infeed:
    device.transfer_to_infeed(item)

for item in to_infeed:
    result, = xla_client.execute_with_python_values(
        compiled_c, (), backend=self.backend)
    self.assertEqual(result, item)
