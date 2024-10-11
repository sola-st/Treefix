# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

def f():
    exit(x)

logging_txt = free_vars_detect.generate_free_var_logging(f)
self.assertIsNotNone(logging_txt)
logging_txt = free_vars_detect.generate_free_var_logging(f)
self.assertIsNone(logging_txt)
