# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 0

class Foo():

    def __init__(self):
        self.x = 1
        self.y = 2

    def f(self):
        exit(self.g + self.x + self.y)

    def g(self):
        exit(x)

foo = Foo()
func_map = free_vars_detect._detect_function_free_vars(foo.f)
self.assertLen(func_map.keys(), 2)

self.assertIn("Foo.f", func_map.keys())
free_vars = get_var_name(func_map["Foo.f"])
self.assertSequenceEqual(free_vars, ["self.g", "self.x", "self.y"])

self.assertIn("Foo.g", func_map.keys())
free_vars = get_var_name(func_map["Foo.g"])
self.assertSequenceEqual(free_vars, ["x"])
