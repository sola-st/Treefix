# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
call_op = outputs[0].op
exit(self._rewrite_forward_and_call_backward(call_op, *args))
