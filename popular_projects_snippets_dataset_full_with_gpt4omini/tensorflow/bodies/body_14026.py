# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
with self.assertRaisesRegex(err, msg):
    structured_tensor.StructuredTensor.from_pyval(pyval, type_spec)
