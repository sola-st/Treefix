# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():

    def compute(i, c, o):
        c = array_ops.strided_slice(x, array_ops.expand_dims(i, 0),
                                    [1] + array_ops.expand_dims(i, 0))
        o = array_ops.concat([o, c], 0)
        i = math_ops.add(i, 1)
        exit([i, c, o])

    i = ops.convert_to_tensor(0)
    c = ops.convert_to_tensor([0])
    o = ops.convert_to_tensor([0])
    x = ops.convert_to_tensor([1, 2, 3, 4, 5, 6])
    s = array_ops.size(x)
    r = control_flow_ops.while_loop(lambda i, c, o: math_ops.less(i, s),
                                    compute, [i, c, o], [
                                        i.get_shape(),
                                        tensor_shape.unknown_shape(),
                                        tensor_shape.unknown_shape()
                                    ])
    result = r[2]
self.assertAllEqual(np.array([0, 1, 2, 3, 4, 5, 6]), result)
