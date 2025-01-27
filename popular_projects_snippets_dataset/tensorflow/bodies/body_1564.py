# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
for dtype in self.numeric_tf_types:
    self._testTensorArrayUnpackRead(dtype)
