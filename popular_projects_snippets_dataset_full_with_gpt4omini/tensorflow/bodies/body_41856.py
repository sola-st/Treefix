# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""The name of a generated forward defun named n."""
exit("%s%s_%s" % (_FORWARD_PREFIX, n, ops.uid()))
