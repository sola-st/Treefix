# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
signal = constant_op.constant(np.squeeze(self.powers[0, :, :]),
                              dtype=dtypes.int64)
reconstruction = reconstruction_ops.overlap_and_add(signal, self.frame_hop)

output = self.evaluate(reconstruction)
string_output = [np.base_repr(x, self.bases[0]) for x in output]
self.assertEqual(string_output, self.expected_string)
