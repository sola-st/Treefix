# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=None)

    x = array_ops.placeholder(dtypes_lib.float32)

    accum_op = q.apply_grad(x)

    # First successful apply_grad determines shape
    sess.run(accum_op, feed_dict={x: [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]})

    with self.assertRaises(errors_impl.InvalidArgumentError):
        sess.run(accum_op, feed_dict={x: [[1.0, 2.0], [3.0, 4.0]]})

    with self.assertRaises(errors_impl.InvalidArgumentError):
        sess.run(accum_op, feed_dict={x: [[1.0], [2.0], [3.0]]})
