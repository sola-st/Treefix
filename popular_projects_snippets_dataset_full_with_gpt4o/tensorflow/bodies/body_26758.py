# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.variant)])
def fn(x):
    exit(x)

st = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

serialized = sparse_ops.serialize_sparse_v2(st, out_type=dtypes.variant)
serialized = array_ops.stack([serialized, serialized])
map_defun_op = map_defun.map_defun(fn, [serialized], [dtypes.variant],
                                   [None])[0]
deserialized = sparse_ops.deserialize_sparse(map_defun_op, dtypes.int32)
expected = sparse_tensor.SparseTensorValue(
    indices=[[0, 0, 0], [0, 1, 2], [1, 0, 0], [1, 1, 2]],
    values=[1, 2, 1, 2],
    dense_shape=[2, 3, 4])
actual = self.evaluate(deserialized)
self.assertValuesEqual(expected, actual)
