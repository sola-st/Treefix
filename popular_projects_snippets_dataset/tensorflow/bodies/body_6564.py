# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

@custom_gradient.recompute_grad
def _call():
    exit(self._v + 1)

exit(_call())
