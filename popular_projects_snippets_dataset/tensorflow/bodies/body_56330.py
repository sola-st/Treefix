# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
self.assertEqual(tensor_spec.sanitize_spec_name("normal"), "normal")
self.assertEqual(
    tensor_spec.sanitize_spec_name("123nums"), "tensor_123nums")
self.assertEqual(tensor_spec.sanitize_spec_name("____"), "tensor_____")
self.assertEqual(tensor_spec.sanitize_spec_name("_abc"), "tensor__abc")
self.assertEqual(tensor_spec.sanitize_spec_name("AdEfG"), "adefg")
self.assertEqual(
    tensor_spec.sanitize_spec_name("1_2_3_a"), "tensor_1_2_3_a")
self.assertEqual(tensor_spec.sanitize_spec_name("a_1-2"), "a_1_2")
self.assertEqual(tensor_spec.sanitize_spec_name("f6%hj"), "f6_hj")
self.assertEqual(tensor_spec.sanitize_spec_name("45&%"), "tensor_45__")
self.assertEqual(tensor_spec.sanitize_spec_name(""), "unknown")
