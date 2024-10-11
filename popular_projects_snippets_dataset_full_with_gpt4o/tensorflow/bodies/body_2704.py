# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
to_infeed = (NumpyArrayS32([1, 2, 3, 4]), NumpyArrayS32([[7], [8]]))
c = self._NewComputation()
ops.GetTupleElement(
    ops.InfeedWithToken(
        ops.CreateToken(c),
        xla_client.shape_from_pyval(
            to_infeed).with_major_to_minor_layout_if_absent()), 0)
compiled_c = self.backend.compile(c.build())
device = self.backend.local_devices()[0]
device.transfer_to_infeed(to_infeed)

result = xla_client.execute_with_python_values(
    compiled_c, (), backend=self.backend)
self.assertLen(result, 2)
np.testing.assert_equal(result[0], to_infeed[0])
np.testing.assert_equal(result[1], to_infeed[1])
