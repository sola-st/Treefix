# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/const_arg_test.py
with self.session() as session:
    with self.test_scope():
        a = array_ops.placeholder(dtypes.int32, [], name="a")
        size = array_ops.reshape(array_ops.where_v2(a >= 0, 1, 0), [1])
        output = xla.dynamic_slice([11, 12, 13], [0], size)
    result = session.run(output, {a: 1})
    expected = [11]
    self.assertEqual(result, expected)
