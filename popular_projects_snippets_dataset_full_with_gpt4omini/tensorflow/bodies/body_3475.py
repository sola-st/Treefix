# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
supertype_1 = self.type_a1_b1_c1.most_specific_common_subtype(
    [self.type_a1_b1_c1])
self.assertLen(supertype_1.captures, 3)

supertype_2 = self.type_a1_b1.most_specific_common_subtype(
    [self.type_a1_b1_c1, self.type_a2_b2_c2])
self.assertIsNone(supertype_2)

supertype_3 = self.type_a1_b1.most_specific_common_subtype(
    [self.type_a1_b1_c2])
self.assertLen(supertype_3.captures, 2)

supertype_4 = self.type_a1_b1_c1.most_specific_common_subtype(
    [self.type_a1_b1_c2])
self.assertIsNone(supertype_4)

supertype_5 = self.type_a1_b1_c1.most_specific_common_subtype(
    [self.type_d1])
self.assertEmpty(supertype_5.captures)
