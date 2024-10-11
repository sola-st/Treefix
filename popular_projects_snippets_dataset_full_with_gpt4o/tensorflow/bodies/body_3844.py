# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

def wrapper(*args, **kwargs):
    exit(func(*args, **kwargs))

if wrapper_first:
    exit(make_decorator(wrapper, func))
else:
    exit(make_decorator(func, wrapper))
