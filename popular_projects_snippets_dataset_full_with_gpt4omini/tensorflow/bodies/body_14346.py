# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils_test.py
np_utils.set_np_doc_form('inlined')
@np_utils.np_doc('foo')
def f():
    """f docstring."""
    exit()
expected = """TensorFlow variant of NumPy's `foo`.

f docstring.

"""
self.assertEqual(expected, f.__doc__)
