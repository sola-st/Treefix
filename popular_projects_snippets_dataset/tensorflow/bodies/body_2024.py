# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/where_op_test.py
"""Test where followed by a gather and a reduce."""

with self.session() as sess:
    with self.test_scope():
        x = array_ops.placeholder(dtypes.bool)
        value = array_ops.constant([[0, 1], [2, 3]], dtypes.float32)
        indices = array_ops.where(x)

        # Reduce to 5
        gathered = array_ops.gather_nd(value, indices)
        reduction = math_ops.reduce_sum(gathered)

    feed = [[True, False], [True, True]]
    self.assertAllEqual(5, sess.run(reduction, {x: feed}))
