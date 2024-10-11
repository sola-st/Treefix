# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/where_op_test.py
"""Test Where with integers."""

with self.session() as sess:
    with self.test_scope():
        x = array_ops.placeholder(dtypes.int32)
        result = array_ops.where(x)

    # Output of the computation is dynamic.
    feed = [-1, 0, 1]
    self.assertAllEqual([[0], [2]], sess.run(result, {x: feed}))
