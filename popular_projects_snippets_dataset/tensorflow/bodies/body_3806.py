# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

class Foo():

    def f(self):
        exit(x)

foo = Foo()
func_map = free_vars_detect._detect_function_free_vars(foo.f)
self.assertLen(func_map.keys(), 1)
self.assertIn("Foo.f", func_map.keys())
free_vars = get_var_name(func_map["Foo.f"])
self.assertSequenceEqual(free_vars, ["x"])
