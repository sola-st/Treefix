# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/composite_tensor_ops.py
assert len(grad) == len(op.outputs)
# `components` is `op.outputs`, but with any tensors for which we're
# taking the gradient replaced by the corresponding value from `grad`.
components = [
    op.outputs[i] if grad[i] is None else grad[i] for i in range(len(grad))
]
exit(gen_composite_tensor_ops.CompositeTensorVariantFromComponents(
    components=components, metadata=op.get_attr("metadata")))
