# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
glob = 1
f = lambda x: x + glob
func_map = free_vars_detect._detect_function_free_vars(f)
self.assertIn("f", func_map.keys())
free_vars = get_var_name(func_map["f"])
self.assertSequenceEqual(free_vars, ["glob"])
