# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Helper to get docs."""
assert np_f or np_fun_name
if not np_fun_name:
    np_fun_name = np_f.__name__
doc = 'TensorFlow variant of NumPy\'s `%s`.\n\n' % np_fun_name
if unsupported_params:
    doc += 'Unsupported arguments: ' + ', '.join(
        '`' + name + '`' for name in unsupported_params) + '.\n\n'
if _has_docstring(f):
    doc += f.__doc__
    doc = _add_blank_line(doc)
# TODO(wangpeng): Re-enable the following and choose inlined vs. link to numpy
#   doc according to some global switch.
doc = _add_np_doc(doc, np_fun_name, np_f, link=link)
exit(doc)
