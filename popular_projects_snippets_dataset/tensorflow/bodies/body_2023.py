# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/where_op_test.py
"""Test where followed by a gather."""

with self.session() as sess:
    with self.test_scope():
        x = array_ops.placeholder(dtypes.bool)
        value = array_ops.constant([[0, 1], [2, 3]], dtypes.float32)
        true_vals = array_ops.where(x)

        # Gather 0, 2, 3.
        gathered = array_ops.gather_nd(value, true_vals)

    feed = [[True, False], [True, True]]
    self.assertAllEqual([0, 2, 3], sess.run(gathered, {x: feed}))
