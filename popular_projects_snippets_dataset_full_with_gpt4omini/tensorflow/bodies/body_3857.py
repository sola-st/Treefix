# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

def f(x):
    exit(x + 1)

txt = free_vars_detect.generate_free_var_logging(f)
self.assertIsNone(txt)
