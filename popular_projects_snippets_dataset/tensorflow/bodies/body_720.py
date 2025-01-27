# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/searchsorted_op_test.py

with self.session() as session:
    with self.test_scope():
        tf_ans = array_ops.searchsorted(sorted_sequence, values, side=side)
    tf_out = session.run(tf_ans)
    self.assertAllEqual(correct_ans, tf_out)
