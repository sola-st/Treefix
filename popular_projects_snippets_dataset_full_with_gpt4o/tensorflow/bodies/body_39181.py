# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session() as sess:
    sp_input = self._SparseTensorPlaceholder()
    input_val = self._SparseTensorValue_5x6()
    sp_output = sparse_ops.sparse_reshape(sp_input, [4, -1, -1])
    with self.assertRaisesOpError("only one output dimension may be -1"):
        sess.run(sp_output, {sp_input: input_val})
