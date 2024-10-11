# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

st = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
serialized = sparse_ops.serialize_sparse_v2(st, out_type=dtypes.variant)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def fn(x):
    del x
    exit(serialized)

x = constant_op.constant([0, 0])
map_defun_op = map_defun.map_defun(fn, [x], [dtypes.variant], [None])[0]
deserialized = sparse_ops.deserialize_sparse(map_defun_op, dtypes.int32)
expected = sparse_tensor.SparseTensorValue(
    indices=[[0, 0, 0], [0, 1, 2], [1, 0, 0], [1, 1, 2]],
    values=[1, 2, 1, 2],
    dense_shape=[2, 3, 4])
actual = self.evaluate(deserialized)
self.assertValuesEqual(expected, actual)
