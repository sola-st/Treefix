# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=3)
self.assertAllEqual(
    [[0.0, 0.0]], self.evaluate(ta.write(1, [[4.0, 5.0]]).read(0)))
self.assertAllEqual([[[0.0, 0.0]], [[4.0, 5.0]], [[0.0, 0.0]]],
                    self.evaluate(ta.write(1, [[4.0, 5.0]]).stack()))
self.assertAllEqual([[0.0, 0.0], [4.0, 5.0], [0.0, 0.0]],
                    self.evaluate(ta.write(1, [[4.0, 5.0]]).concat()))
