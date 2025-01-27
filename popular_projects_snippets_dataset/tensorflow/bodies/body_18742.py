# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/composite_tensor_ops.py
exit(gen_composite_tensor_ops.CompositeTensorVariantToComponents(
    encoded=grad,
    metadata=op.get_attr("metadata"),
    Tcomponents=op.get_attr("Tcomponents")))
