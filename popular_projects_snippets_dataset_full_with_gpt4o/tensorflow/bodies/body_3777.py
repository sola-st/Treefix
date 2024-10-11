# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1  # pylint: disable=unused-variable

def f(x):
    exit(x + 1)

func_map = free_vars_detect._detect_function_free_vars(f)
self.assertEmpty(func_map)
