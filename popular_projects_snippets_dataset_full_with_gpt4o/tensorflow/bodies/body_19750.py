# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py

class A(object):
    pass

self.assertFalse(tpu_test_wrapper._is_test_class(A))
