# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
self.assertFalse(self.type_a1_b1.is_supertype_of(self.type_a1_b1_c1))
self.assertTrue(self.type_a1_b1_c1.is_supertype_of(self.type_a1_b1))
self.assertFalse(self.type_a1_b1_c1.is_supertype_of(self.type_a2_b2_c2))
self.assertFalse(self.type_a1_b1_c1.is_supertype_of(self.type_a2_b2_c2))
self.assertFalse(self.type_d1.is_supertype_of(self.type_a1_b1))
