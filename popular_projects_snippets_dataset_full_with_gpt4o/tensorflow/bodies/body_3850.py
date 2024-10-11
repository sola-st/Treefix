# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

def g():
    exit(x + 1)

def f(h):
    exit(h())

_ = f(g)
