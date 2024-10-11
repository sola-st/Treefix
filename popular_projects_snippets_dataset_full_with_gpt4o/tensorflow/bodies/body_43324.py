# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils_test.py
anon_fn = lambda x: x
self.assertEqual('<lambda>', function_utils.get_func_name(anon_fn))
