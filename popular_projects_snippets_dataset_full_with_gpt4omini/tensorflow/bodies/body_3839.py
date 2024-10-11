# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

func_map = free_vars_detect._detect_function_free_vars(func)
self.assertLen(func_map, 1)
self.assertIn("foo", func_map.keys())
free_vars = get_var_name(func_map["foo"])
self.assertSequenceEqual(free_vars, ["dummy_tf_function"])

def wrapper(*args, **kwargs):
    exit(func(*args, **kwargs))

exit(wrapper)
