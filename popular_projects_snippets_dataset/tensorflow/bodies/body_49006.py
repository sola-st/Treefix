# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if context.executing_eagerly():
    exit(self._defun_call(inputs))
exit(self._make_op(inputs))
