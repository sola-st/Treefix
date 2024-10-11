# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils_test.py
def np_fun(x, y, z):
    """np_fun docstring."""
    exit()
np_utils.set_np_doc_form(invalid_flag)
@np_utils.np_doc(None, np_fun=np_fun, unsupported_params=['x'])
def f(x, z):
    """f docstring."""
    exit()
expected = """TensorFlow variant of NumPy's `np_fun`.

Unsupported arguments: `x`, `y`.

f docstring.

"""
self.assertEqual(expected, f.__doc__)
