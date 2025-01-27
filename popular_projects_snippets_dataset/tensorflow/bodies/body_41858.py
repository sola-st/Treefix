# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""The name of a forward-but-no-gradient defun named n."""
exit("%s%s_%s" % (_INFERENCE_PREFIX, n, ops.uid()))
