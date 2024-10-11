# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops_test.py
values = tensor_array_ops.TensorArray(
    size=4, dtype=dtypes.string, element_shape=[None], infer_shape=False)
a = array_ops.placeholder(dtypes.string, [
    None,
])
b = array_ops.placeholder(dtypes.string, [
    None,
])
values = (values.write(0, a).write(
    1, constant_op.constant([], dtypes.string))).write(2, b).write(
        3, constant_op.constant([], dtypes.string))

with self.session() as s:
    result = s.run(values.concat(), {a: ['a', 'b', 'c'], b: ['c', 'd', 'e']})
self.assertAllEqual(result, [b'a', b'b', b'c', b'c', b'd', b'e'])
