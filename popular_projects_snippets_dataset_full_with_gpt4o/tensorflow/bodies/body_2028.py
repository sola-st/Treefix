# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/where_op_test.py
"""Test Where with floats."""

with self.session() as sess:
    with self.test_scope():
        x = array_ops.placeholder(dtypes.complex64)
        result = array_ops.where(x)

    # Output of the computation is dynamic.
    feed = [
        -1.0 + 0.0j, -0.0 + 0.0j, 0.0 - 0.0j, 1.0 - 1.0j, 1.0 + 0.0j,
        0.0 + 1.0j
    ]
    self.assertAllEqual([[0], [3], [4], [5]], sess.run(result, {x: feed}))
