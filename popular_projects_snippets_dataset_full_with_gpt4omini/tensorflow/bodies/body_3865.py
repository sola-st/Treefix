# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 0

class Foo():

    def f(self):
        exit(self.g)

    def g(self):
        exit([x])

foo = Foo()
txt = free_vars_detect.generate_free_var_logging(foo.f)
txt = self._remove_explanation(txt)
lines = txt.split("\n")
self.assertLen(lines, 2)
self.assertEqual(lines[0], "Inside function Foo.f(): self.g")
self.assertEqual(lines[1], "Inside function Foo.g(): x")
