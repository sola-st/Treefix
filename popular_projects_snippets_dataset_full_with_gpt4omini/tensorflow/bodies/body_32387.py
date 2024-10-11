# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
input_matrix = np.squeeze(self.powers[0, :, :])
input_matrix = input_matrix[np.newaxis, :, :].astype(float)
signal = constant_op.constant(input_matrix, dtype=dtypes.float32)
reconstruction = reconstruction_ops.overlap_and_add(signal, self.frame_hop)

output = self.evaluate(reconstruction)

string_output = [np.base_repr(int(x), self.bases[0]) for x in
                 np.squeeze(output)]

self.assertEqual(output.shape, (1, 9))
self.assertEqual(string_output, self.expected_string)
