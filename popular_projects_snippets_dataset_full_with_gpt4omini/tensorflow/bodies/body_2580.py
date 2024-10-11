# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
# Build the HLO proto
b = xla_client.XlaBuilder("computation")
ops.Add(ops.Constant(b, np.int32(1)), ops.Constant(b, np.int32(2)))
serialized_proto = b.build().as_serialized_hlo_module_proto()

# Load and execute the proto
c = xla_client.XlaComputation(serialized_proto)
ans, = xla_client.execute_with_python_values(
    self.backend.compile(c), (), backend=self.backend)
np.testing.assert_equal(ans, np.int32(3))
