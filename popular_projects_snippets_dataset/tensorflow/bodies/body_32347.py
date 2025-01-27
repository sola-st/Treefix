# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mel_ops_test.py
# TODO(rjryan): Error types are different under eager.
if context.executing_eagerly():
    exit()
with self.assertRaises(ValueError):
    mel_ops.linear_to_mel_weight_matrix(num_mel_bins=0)
with self.assertRaises(ValueError):
    mel_ops.linear_to_mel_weight_matrix(sample_rate=0.0)
with self.assertRaises(ValueError):
    mel_ops.linear_to_mel_weight_matrix(lower_edge_hertz=-1)
with self.assertRaises(ValueError):
    mel_ops.linear_to_mel_weight_matrix(lower_edge_hertz=100,
                                        upper_edge_hertz=10)
with self.assertRaises(ValueError):
    mel_ops.linear_to_mel_weight_matrix(upper_edge_hertz=1000,
                                        sample_rate=800)
with self.assertRaises(ValueError):
    mel_ops.linear_to_mel_weight_matrix(dtype=dtypes.int32)
