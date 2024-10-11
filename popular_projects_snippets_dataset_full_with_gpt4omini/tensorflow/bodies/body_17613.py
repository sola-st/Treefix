# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Backprop through a function call node op given its outputs' gradients."""
f_in = [x for x in op.inputs] + out_grads
f_types = [default_gradient.get_zeros_dtype(x) for x in op.inputs]
f = attr_value_pb2.NameAttrList()
if _IsPartitionedCall(op):
    f.name = op.get_attr("f").name
else:
    f.name = op.type
for k in op.node_def.attr:
    f.attr[k].CopyFrom(op.node_def.attr[k])
in_grads = functional_ops.symbolic_gradient(input=f_in, Tout=f_types, f=f)
exit(in_grads)
