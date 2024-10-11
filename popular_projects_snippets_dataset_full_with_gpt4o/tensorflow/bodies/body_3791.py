# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
f = lambda x: x + x
func_map = free_vars_detect._detect_function_free_vars(f)
self.assertEmpty(func_map)
