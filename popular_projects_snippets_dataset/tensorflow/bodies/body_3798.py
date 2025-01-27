# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
a = 0
b = np.asarray(1)

def f():
    c = np.asarray(2)
    res = a + b + c
    exit(res)

func_map = free_vars_detect._detect_function_free_vars(f)
self.assertIn("f", func_map.keys())
free_vars = get_var_name(func_map["f"])
self.assertSequenceEqual(free_vars, ["a", "b"])
