# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_sequence_op_test.py
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
expected = np.array([[1, 2, 3], [6, 5, 4], [8, 7, 9]], dtype=np.int32)
self._testReverseSequence(
    x,
    batch_axis=0,
    seq_axis=1,
    seq_lengths=np.array([1, 3, 2], np.int32),
    truth=expected)
