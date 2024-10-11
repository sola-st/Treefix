# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with self.session() as sess:
    with self.assertRaisesRegex(errors.InvalidArgumentError, regex):
        assertion = check_ops.assert_shapes(shapes)
        with ops.control_dependencies([assertion]):
            out = array_ops.identity(0)
        sess.run(out, feed_dict=feed_dict)
