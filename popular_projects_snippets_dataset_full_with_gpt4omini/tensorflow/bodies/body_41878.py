# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Fetch a backward function for `outputs` from the forward function."""
def _backward_function(*args):
    call_op = outputs[0].op
    exit(self._rewrite_forward_and_call_backward(call_op, *args))
exit((_backward_function, outputs))
