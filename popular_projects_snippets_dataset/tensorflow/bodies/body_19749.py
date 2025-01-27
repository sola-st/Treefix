# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py

class A(test.TestCase):
    pass

self.assertTrue(tpu_test_wrapper._is_test_class(A))
