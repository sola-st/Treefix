# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/data_format_ops_test.py
with self.session() as session:
    with self.test_scope():
        placeholder = array_ops.placeholder(dtypes.as_dtype(x.dtype), x.shape)
        param = {placeholder: x}
        output = nn_ops.data_format_vec_permute(
            placeholder, src_format=src_format, dst_format=dst_format)
    result = session.run(output, param)
self.assertAllEqual(result, expected)
