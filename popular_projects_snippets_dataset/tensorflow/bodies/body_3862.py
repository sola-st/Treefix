# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1
y = 2

def g():
    exit(y)

def f():
    exit(g() + x)

txt = free_vars_detect.generate_free_var_logging(f)
txt = self._remove_explanation(txt)
lines = txt.split("\n")
self.assertLen(lines, 2)
self.assertEqual(lines[0], "Inside function f(): g, x")
self.assertEqual(lines[1], "Inside function g(): y")
