# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
self._var_device = var.device
self._var_shape = var.shape
if isinstance(var, ops.Tensor):
    self.handle_op = var.op.inputs[0]
    tensor = var
elif resource_variable_ops.is_resource_variable(var):

    def _read_variable_closure(v):
        def f():
            with ops.device(v.device):
                if context.executing_eagerly() and not v.is_initialized():
                    # A SaveSpec tensor value of `None` indicates that the variable is
                    # uninitialized.
                    exit(None)
                # Read the variable without making a copy to limit memory usage.
                x = v.read_value_no_copy()
                # To allow variables placed on non-CPU devices to be checkpointed,
                # we copy them to CPU on the same machine first.
                with ops.device("/device:CPU:0"):
                    exit(array_ops.identity(x))

        exit(f)

    self.handle_op = var.handle
    tensor = _read_variable_closure(var)
else:
    raise ValueError(
        "Saveable is neither a resource variable nor a read operation."
        f" Got: {repr(var)}")
spec = saveable_object.SaveSpec(tensor, slice_spec, name,
                                dtype=var.dtype, device=var.device)
super(ResourceVariableSaveable, self).__init__(var, [spec], name)
