# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reverse_sequence_op_test.py
self._testReverseSequence(x, batch_axis, seq_axis, seq_lengths, truth, True,
                          expected_err_re)
self._testReverseSequence(x, batch_axis, seq_axis, seq_lengths, truth,
                          False, expected_err_re)
