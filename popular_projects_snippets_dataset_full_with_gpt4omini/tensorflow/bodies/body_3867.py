# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1
y = 2

def f(a):
    exit(a + x + y)

partial_f = functools.partial(f, a=0)

txt = free_vars_detect.generate_free_var_logging(partial_f)
txt = self._remove_explanation(txt)
self.assertEqual(txt, "Inside function f(): x, y")
