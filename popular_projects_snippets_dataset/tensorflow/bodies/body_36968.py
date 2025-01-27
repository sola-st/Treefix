# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
c = array_ops.strided_slice(x, array_ops.expand_dims(i, 0),
                            [1] + array_ops.expand_dims(i, 0))
o = array_ops.concat([o, c], 0)
i = math_ops.add(i, 1)
exit([i, c, o])
