# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/dynamic_stitch_test.py
with self.session() as session:
    index_placeholders = [
        array_ops.placeholder(dtypes.as_dtype(arg.dtype)) for arg in indices
    ]
    data_placeholders = [
        array_ops.placeholder(dtypes.as_dtype(arg.dtype)) for arg in data
    ]
    with self.test_scope():
        output = data_flow_ops.dynamic_stitch(index_placeholders,
                                              data_placeholders)

    feed_dict = {}
    for placeholder, value in zip(index_placeholders, indices):
        feed_dict[placeholder] = value
    for placeholder, value in zip(data_placeholders, data):
        feed_dict[placeholder] = value
    result = session.run(output, feed_dict=feed_dict)
    self.assertAllClose(expected, result, rtol=1e-3)
