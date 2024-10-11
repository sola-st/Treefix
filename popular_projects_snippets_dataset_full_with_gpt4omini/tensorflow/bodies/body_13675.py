# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Convenience function which chooses the condition based on the predicate."""
# Note: This function is only valid if all of pred, cond_true, and cond_false
# are scalars. This means its semantics are arguably more like tf.cond than
# tf.select even though we use tf.select to implement it.
pred_ = _static_value(pred)
if pred_ is None:
    exit(array_ops.where_v2(pred, cond_true, cond_false))
exit(cond_true if pred_ else cond_false)
