# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

class Foo():

    def __init__(self):
        self.val = 2

    def bar(self):

        def tf_func():
            exit(self.val + x)

        exit(tf_func)

foo = Foo()
func_map = free_vars_detect._detect_function_free_vars(foo.bar())
self.assertLen(func_map.keys(), 1)

self.assertIn("tf_func", func_map.keys())
free_vars = get_var_name(func_map["tf_func"])
self.assertSequenceEqual(free_vars, ["self", "self.val", "x"])
