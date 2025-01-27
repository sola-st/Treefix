# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

def f():

    def g():
        exit(x + 1)

    exit(g())

func_map = free_vars_detect._detect_function_free_vars(f)
self.assertIn("f", func_map.keys())
self.assertLen(func_map.keys(), 1)
free_vars = get_var_name(func_map["f"])
self.assertSequenceEqual(free_vars, ["x"])
