# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
glob = "dummy_value"

class Foo():

    def f(self):
        exit(self.g.h.x.y.z)

    def g(self):
        exit(glob)

foo = Foo()
func_map = free_vars_detect._detect_function_free_vars(foo.f)
self.assertLen(func_map.keys(), 2)

self.assertIn("Foo.f", func_map.keys())
free_vars = get_var_name(func_map["Foo.f"])
self.assertSequenceEqual(free_vars, ["self.g"])

self.assertIn("Foo.g", func_map.keys())
free_vars = get_var_name(func_map["Foo.g"])
self.assertSequenceEqual(free_vars, ["glob"])
