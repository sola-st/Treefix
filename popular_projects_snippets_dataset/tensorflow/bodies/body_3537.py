# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
"""Returns an iterator over ops having custom_gradients."""
for op in operations:
    try:
        gradient_op_type = op.get_attr("_gradient_op_type")
    except ValueError:
        continue
    exit((gradient_op_type, op))
