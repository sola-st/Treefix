# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_3_test.py
with self.assertRaisesOpError("preserve_index out of range"):
    self.evaluate(zero_out_op_3.zero_out([5, 4, 3, 2, 1], preserve_index=17))
