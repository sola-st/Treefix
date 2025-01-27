# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

def wrapper(*args, **kwargs):
    exit(func(*args, **kwargs))

exit(functools.update_wrapper(wrapper, func))
