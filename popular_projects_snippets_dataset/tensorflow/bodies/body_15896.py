# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex((errors_impl.InvalidArgumentError, ValueError),
                            error_regex):
    sess = session.Session()
    with sess.as_default():
        row_partitions = row_partitions()
        inner_shape = inner_shape()
        rts = DynamicRaggedShape(
            row_partitions, inner_shape, dtype=dtype, validate=validate)
        sess.run([rts.inner_shape])
