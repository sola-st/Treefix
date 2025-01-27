# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st2 = StructuredTensor.from_pyval(st)
expected2 = StructuredTensor.from_pyval(expected)
result = st2.promote(source_path, new_field_name)
self.assertAllEqual(result, expected2)
