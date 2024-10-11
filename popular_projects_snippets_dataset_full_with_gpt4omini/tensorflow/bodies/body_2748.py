# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
devices_by_kind = collections.defaultdict(list)
for device in self.backend.devices():
    devices_by_kind[device.device_kind].append(device)
multi_devices = [d for d in devices_by_kind.values() if len(d) > 1]
if not multi_devices:
    raise unittest.SkipTest("Test needs multiple identical devices")
devices = multi_devices[0]

c = self._NewComputation()
args = [
    np.array(3, dtype=np.int32),
    np.array([10, 15, -2, 7], dtype=np.int32)
]
p0 = ops.Parameter(c, 0, xla_client.shape_from_pyval(args[0]))
p1 = ops.Parameter(c, 1, xla_client.shape_from_pyval(args[1]))
ops.Mul(p0, p1)
options = xla_client.CompileOptions()
options.compile_portable_executable = True
compiled_c = self.backend.compile(c.build(), compile_options=options)
for device in devices:
    out, = compiled_c.execute(
        [self.backend.buffer_from_pyval(a, device=device) for a in args],
        device=device)
    np.testing.assert_array_equal(np.asarray(out), args[0] * args[1])
