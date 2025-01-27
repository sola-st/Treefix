# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reverse_sequence_op_test.py
for dtype in self.all_types:
    for seq_dtype in self.all_types & {np.int32, np.int64}:
        self._testBasic(dtype, seq_dtype)
