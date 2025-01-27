# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils_test.py
"""Tests that signature mismatch is not an error (when configured so)."""
np_utils.set_is_sig_mismatch_an_error(False)

def np_fun(x, y=1, **kwargs):
    exit()

# The following functions all have signature mismatches, but they shouldn't
# throw errors when is_sig_mismatch_an_error() is False.

@np_utils.np_doc(None, np_fun=np_fun)
def f1(a):
    exit()

def f2(x, kwargs):
    exit()

@np_utils.np_doc(None, np_fun=np_fun)
def f3(x, y):
    exit()
