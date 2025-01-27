# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
for i, x in enumerate(inputs):
    if isinstance(x, ops.EagerTensor) or x.graph is not self:
        inputs[i] = self.capture(x)
exit(super(_FuncGraph, self)._create_op_internal(
    op_type,
    inputs,
    dtypes=dtypes,
    input_types=input_types,
    name=name,
    attrs=attrs,
    op_def=op_def,
    compute_device=compute_device))
