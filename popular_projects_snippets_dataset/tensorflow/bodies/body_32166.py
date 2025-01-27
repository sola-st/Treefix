# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
strings = ["hello.cruel,world", "hello cruel world"]

with self.cached_session() as sess:
    delimiter = array_ops.placeholder(dtypes.string)

    tokens = string_ops.string_split(strings, delimiter=delimiter)

    with self.assertRaises(errors_impl.InvalidArgumentError):
        sess.run(tokens, feed_dict={delimiter: ["a", "b"]})
    with self.assertRaises(errors_impl.InvalidArgumentError):
        sess.run(tokens, feed_dict={delimiter: ["a"]})
    indices, values, shape = sess.run(tokens, feed_dict={delimiter: ".,"})

    self.assertAllEqual(indices, [[0, 0], [0, 1], [0, 2], [1, 0]])
    self.assertAllEqual(values,
                        [b"hello", b"cruel", b"world", b"hello cruel world"])
    self.assertAllEqual(shape, [2, 3])
