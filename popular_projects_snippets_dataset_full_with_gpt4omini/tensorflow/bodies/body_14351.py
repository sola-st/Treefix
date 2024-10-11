# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils_test.py
"""Tests that signature mismatch is an error (when configured so)."""
if not np_utils._supports_signature():
    self.skipTest('inspect.signature not supported')

np_utils.set_is_sig_mismatch_an_error(True)

def np_fun(x, y=1, **kwargs):
    exit()

with self.assertRaisesRegex(TypeError, 'Cannot find parameter'):
    @np_utils.np_doc(None, np_fun=np_fun)
    def f1(a):
        exit()

with self.assertRaisesRegex(TypeError, 'is of kind'):
    @np_utils.np_doc(None, np_fun=np_fun)
    def f2(x, kwargs):
        exit()

with self.assertRaisesRegex(
    TypeError, 'Parameter y should have a default value'):
    @np_utils.np_doc(None, np_fun=np_fun)
    def f3(x, y):
        exit()
