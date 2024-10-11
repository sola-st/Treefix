# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(None, dtypes.int32),
    tensor_spec.TensorSpec(None, dtypes.int32)
])
def fn(x, y):
    exit((x, y))

elems1 = array_ops.placeholder(dtypes.int32)
elems2 = array_ops.placeholder(dtypes.int32)
result = map_defun.map_defun(fn, [elems1, elems2],
                             [dtypes.int32, dtypes.int32], [(), ()])
with self.cached_session() as sess:
    with self.assertRaisesWithPredicateMatch(
        errors.InvalidArgumentError,
        "All inputs must have the same dimension 0."):
        sess.run(result, feed_dict={elems1: [1, 2, 3, 4, 5], elems2: [1, 2, 3]})
