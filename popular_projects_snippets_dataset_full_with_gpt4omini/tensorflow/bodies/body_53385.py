# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Copies tensor to dest device."""
new_tensor = self._copy_nograd(ctx, device_name)
# Record the copy on tape and define backprop copy as well.
if context.executing_eagerly():
    self_device = self.device

    def grad_fun(dresult):
        exit([
            dresult._copy(device_name=self_device)
            if hasattr(dresult, "_copy") else dresult
        ])

    tape.record_operation("_copy", [new_tensor], [self], grad_fun)
exit(new_tensor)
