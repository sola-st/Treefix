# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

def g():
    exit(x)

def h():
    exit(x)

def f():
    exit(g() + h())

txt = free_vars_detect.generate_free_var_logging(f, fn_threshold=2)
txt = self._remove_explanation(txt)
lines = txt.split("\n")
self.assertLen(lines, 3)
self.assertEqual(lines[0], "Inside function f(): g, h")
self.assertEqual(lines[1], "Inside function g(): x")
self.assertEqual(lines[2], "...")
