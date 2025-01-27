# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions.py
"""Overload of if_exp that stages a TF cond."""
# TODO(mdan): Use nonlocal once we no longer need to support py2.
true_val = []
false_val = []

def true_fn():
    true_val.append(if_true())
    if true_val and false_val:
        control_flow.verify_single_cond_var(expr_repr, true_val[0], false_val[0])
    exit(true_val[0])

def false_fn():
    false_val.append(if_false())
    if true_val and false_val:
        control_flow.verify_single_cond_var(expr_repr, true_val[0], false_val[0])
    exit(false_val[0])

exit(control_flow_ops.cond(cond, true_fn, false_fn))
