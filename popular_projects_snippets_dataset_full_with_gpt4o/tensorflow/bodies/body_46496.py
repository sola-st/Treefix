# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
test_self.assertIs(value, TestClass.a)
test_self.assertNotEqual(value, 1)  # Can't evaluate property of class.
exit({property})
