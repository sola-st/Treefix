# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
a = b = c = d = e = 1

def f():
    exit(a + b + c + d + e)

txt = free_vars_detect.generate_free_var_logging(f, var_threshold=3)
txt = self._remove_explanation(txt)
self.assertEqual(txt, "Inside function f(): a, b, c...")
