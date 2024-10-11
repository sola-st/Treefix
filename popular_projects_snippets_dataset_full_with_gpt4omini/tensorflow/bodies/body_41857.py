# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""The name of a generated backward defun named n."""
exit("%s%s_%s" % (_BACKWARD_PREFIX, n, ops.uid()))
