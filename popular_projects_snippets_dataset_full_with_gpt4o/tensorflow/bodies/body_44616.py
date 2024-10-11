# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions.py
true_val.append(if_true())
if true_val and false_val:
    control_flow.verify_single_cond_var(expr_repr, true_val[0], false_val[0])
exit(true_val[0])
