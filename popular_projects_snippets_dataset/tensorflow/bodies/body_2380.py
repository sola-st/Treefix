# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
"""Tests that the output of 'tf_reduce_fn' matches numpy's output."""

for test_input in test_inputs:
    with self.session() as sess:
        with self.test_scope():
            a = array_ops.placeholder(dtype)
            index = array_ops.placeholder(index_dtype)
            out = tf_reduce_fn(a, index)
        result = sess.run(out, {a: test_input, index: [0]})
        self.assertAllClose(
            result, np_reduce_fn(test_input, axis=0), rtol=rtol, atol=atol)

        result = sess.run(out, {a: test_input, index: [1]})
        self.assertAllClose(
            result, np_reduce_fn(test_input, axis=1), rtol=rtol, atol=atol)

        result = sess.run(out, {a: test_input, index: [-1]})
        self.assertAllClose(
            result, np_reduce_fn(test_input, axis=1), rtol=rtol, atol=atol)

        # MLIR bridge doesn't return the same error so it can't be matched
        # directly.
        if not test_util.is_mlir_bridge_enabled():
            with self.assertRaisesWithPredicateMatch(
                errors_impl.InvalidArgumentError, 'Invalid reduction dim'):
                sess.run(out, {a: test_input, index: [-33]})

            with self.assertRaisesWithPredicateMatch(
                errors_impl.InvalidArgumentError, 'Invalid reduction dim'):
                sess.run(out, {a: test_input, index: [2]})
