# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform != "tpu":
    self.skipTest("Test requires tpu platform")

c = self._NewComputation()
ops.Add(
    ops.Constant(c, NumpyArrayS32([1, 2])),
    ops.Constant(c, NumpyArrayS32([3, 4])))

options = xla_client.CompileOptions()
executable = self.backend.compile(c.build(), options)
self.assertLen(executable.hlo_modules(), 1)

serialized = self.backend.serialize_executable(executable)
deserialized = self.backend.deserialize_executable(
    serialized,
    executable.hlo_modules()[0], options)

expected, = xla_client.execute_with_python_values(executable, (),
                                                  self.backend)
actual, = xla_client.execute_with_python_values(deserialized, (),
                                                self.backend)
self.assertTrue(np.all(actual == expected))
