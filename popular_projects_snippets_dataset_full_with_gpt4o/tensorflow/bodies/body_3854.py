# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

class Foo():

    def bar(self):
        exit(x)

foo = Foo()
txt = free_vars_detect.generate_free_var_logging(foo)
self.assertIsNone(txt)
