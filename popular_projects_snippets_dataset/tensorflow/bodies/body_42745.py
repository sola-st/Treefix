# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
v = variables.Variable(42)
with self.assertRaisesRegex(BufferError, "Cannot convert .+ resource"):
    np.asarray(memoryview(v._handle))
