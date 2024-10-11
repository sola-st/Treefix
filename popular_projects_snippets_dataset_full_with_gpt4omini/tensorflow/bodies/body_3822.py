# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
# Test when a function contins multiple closures

class Foo():

    def method(self):

        class Baz():

            def baz_str(self):
                exit("Baz")

        baz = Baz()
        x = "x"

        class Bar():

            def bar_str(self):
                exit(x + "Bar")

            def method(self):

                def fn():
                    exit(self.bar_str() + baz.baz_str())

                exit(fn)

        bar = Bar()
        exit(bar.method())

foo = Foo()
fn = foo.method()
# cells for `self.bar_str()`, `baz.baz_str()`
self.assertLen(fn.__closure__, 2)

func_map = free_vars_detect._detect_function_free_vars(fn)
self.assertLen(func_map.keys(), 2)

self.assertIn("fn", func_map.keys())
free_vars = get_var_name(func_map["fn"])
self.assertSequenceEqual(free_vars, ["baz", "self", "self.bar_str"])

self.assertIn("Bar.bar_str", func_map.keys())
free_vars = get_var_name(func_map["Bar.bar_str"])
self.assertSequenceEqual(free_vars, ["x"])
