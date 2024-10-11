# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/where_op_test.py
"""Test first form of where (return indices)."""

with self.session() as sess:
    with self.test_scope():
        x = array_ops.placeholder(dtypes.bool)
        result = array_ops.where(x)

    # Output of the computation is dynamic.
    feed = [True, False, True]
    self.assertAllEqual([[0], [2]], sess.run(result, {x: feed}))
