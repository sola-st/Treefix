# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/where_op_test.py
"""Test Where with floats."""

with self.session() as sess:
    with self.test_scope():
        x = array_ops.placeholder(dtypes.float32)
        result = array_ops.where(x)

    # Output of the computation is dynamic.
    feed = [-1.0, -0.0, 0.0, 1.0]
    self.assertAllEqual([[0], [3]], sess.run(result, {x: feed}))
