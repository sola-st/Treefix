# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
if not test.is_gpu_available():
    exit()
with self.session(force_gpu=True) as sess:
    value = array_ops.placeholder(dtypes.int64)
    ta = tensor_array_ops.TensorArray(dtype=dtypes.int64, size=2)
    ta = ta.scatter([0, 1], value)
    r0 = ta.read(0)
    r1 = ta.read(1)
    v0, v1 = sess.run([r0, r1], feed_dict={value: [-3, 100]})
    self.assertAllEqual(v0, -3)
    self.assertAllEqual(v1, 100)
