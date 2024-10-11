# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session() as sess:
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32,
        tensor_array_name="foo",
        size=3)
    val = array_ops.placeholder(dtypes.float32)
    self.assertAllEqual(
        [[0.0, 0.0]], sess.run(ta.write(1, val).read(0), {val: [[4.0, 5.0]]}))
