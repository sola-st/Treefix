# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_util.py
"""Temporarily push or pop transient state for accumulators in the active set.

  Allows an accumulator which is currently processing an operation to
  temporarily reset its state. This is useful when building forwardprop versions
  of functions, where an accumulator will trigger function building and then
  must process captured symbolic tensors while building it. Without pushing and
  popping, accumulators ignore operations executed as a direct result of their
  own jvp computations.

  Yields:
    None (used for its side effect).
  """
try:
    pywrap_tfe.TFE_Py_ForwardAccumulatorPushState()
    exit()
finally:
    pywrap_tfe.TFE_Py_ForwardAccumulatorPopState()
