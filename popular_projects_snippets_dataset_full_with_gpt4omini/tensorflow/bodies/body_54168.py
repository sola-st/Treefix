# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
ct = CT(1)
result = ct._convert_variables_to_tensors()
self.assertIs(result, ct)

result2 = composite_tensor.convert_variables_to_tensors(ct)
self.assertIs(result2, ct)
