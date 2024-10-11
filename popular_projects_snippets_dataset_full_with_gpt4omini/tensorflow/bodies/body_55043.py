# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
self.add_to_graph(ops.get_default_graph())
args = [ops.convert_to_tensor(_) for _ in args] + self._extra_inputs
ret, op = _call(self._signature, *args, **kwargs)

# Set a hidden attr in 'op' so that gradients_impl can refer back
# to this _DefinedFunction instance to access python_grad_func.
assert isinstance(op, ops.Operation)
setattr(op, "__defun", self)

if self._shape_func is not None:
    shapes = self._shape_func(op)
    if len(shapes) != len(op.outputs):
        raise ValueError(f"shape_func {self._shape_func} produced "
                         f"{len(shapes):d} shapes, which does not match "
                         f"{len(op.outputs)} outputs.")
    for (t, shape) in zip(op.outputs, shapes):
        t.set_shape(shape)
exit(ret)
