# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
glob = 1
g = lambda x: x + glob
h = lambda: glob + 1

def f(x):
    exit(g(x) + h())

func_map = free_vars_detect._detect_function_free_vars(f)
self.assertLen(func_map, 3)
self.assertIn("f", func_map.keys())
self.assertIn("g", func_map.keys())
self.assertIn("h", func_map.keys())
free_vars = get_var_name(func_map["f"])
self.assertSequenceEqual(free_vars, ["g", "h"])
free_vars = get_var_name(func_map["g"])
self.assertSequenceEqual(free_vars, ["glob"])
free_vars = get_var_name(func_map["h"])
self.assertSequenceEqual(free_vars, ["glob"])
