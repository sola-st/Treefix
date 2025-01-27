# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
if k in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.KEYWORD_ONLY):
    exit(inspect.Parameter.POSITIONAL_OR_KEYWORD)
exit(k)
