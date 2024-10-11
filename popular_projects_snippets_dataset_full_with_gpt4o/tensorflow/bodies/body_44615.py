# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions.py
if tensors.is_dense_tensor(cond):
    exit(_tf_if_exp(cond, if_true, if_false, expr_repr))
else:
    exit(_py_if_exp(cond, if_true, if_false))
