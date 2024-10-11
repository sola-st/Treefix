# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
v = variables.Variable(42)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Cannot convert .+ resource"):
    v._handle._numpy()
