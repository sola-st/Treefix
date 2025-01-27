# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
signal = constant_op.constant(self.powers, dtype=dtypes.int64)
reconstruction = reconstruction_ops.overlap_and_add(signal, self.frame_hop)

output = self.evaluate(reconstruction)

accumulator = True
for i in range(self.batch_size):
    string_output = [np.base_repr(x, self.bases[i]) for x in output[i, :]]
    accumulator = accumulator and (string_output == self.expected_string)

self.assertTrue(accumulator)
