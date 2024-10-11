# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
glob = 1

class Foo():

    @classmethod
    def f(cls):
        exit(glob)

func_map = free_vars_detect._detect_function_free_vars(Foo.f)
self.assertLen(func_map.keys(), 1)
self.assertIn("Foo.f", func_map.keys())
free_vars = get_var_name(func_map["Foo.f"])
self.assertSequenceEqual(free_vars, ["glob"])
