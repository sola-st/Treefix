# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
f.__doc__ = _np_doc_helper(f, np_fun, np_fun_name=np_fun_name)
if export:
    exit(np_export.np_export(np_fun_name)(f))
else:
    exit(f)
