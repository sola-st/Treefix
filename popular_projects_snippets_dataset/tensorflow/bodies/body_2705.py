# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
to_round_trip = NumpyArrayS32([1, 2, 3, 4])
c = self._NewComputation()
x_and_token = ops.InfeedWithToken(
    ops.CreateToken(c),
    xla_client.shape_from_pyval(
        to_round_trip[0]).with_major_to_minor_layout_if_absent())
x = ops.GetTupleElement(x_and_token, 0)
token = ops.GetTupleElement(x_and_token, 1)
outfeed_shape = xla_client.shape_from_pyval(
    to_round_trip[0]).with_major_to_minor_layout_if_absent()
ops.OutfeedWithToken(x, token, outfeed_shape)

compiled_c = self.backend.compile(c.build())
device = self.backend.local_devices()[0]

for want in to_round_trip:
    execution = threading.Thread(target=lambda: compiled_c.execute([]))
    execution.start()
    device.transfer_to_infeed(want)
    got = device.transfer_from_outfeed(outfeed_shape)
    execution.join()
    self.assertEqual(want, got)
