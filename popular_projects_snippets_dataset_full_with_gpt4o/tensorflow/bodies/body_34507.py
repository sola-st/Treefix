# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    ta = tensor_array_ops.TensorArray(
        dtype=tf_dtype, tensor_array_name="foo", size=3, infer_shape=False)

    convert = _make_converter(tf_dtype)

    w0 = ta.write(0, convert([[4.0, 5.0], [104.0, 105.0], [204.0, 205.0]]))
    w1 = w0.write(1, convert([[6.0, 7.0], [106.0, 107.0]]))
    w2 = w1.write(2, convert([[8.0, 9.0]]))

    c0 = w2.concat()

    c0 = self.evaluate(c0)
    self.assertAllEqual(
        convert([[4.0, 5.0], [104.0, 105.0], [204.0, 205.0], [6.0, 7.0],
                 [106.0, 107.0], [8.0, 9.0]]), c0)
