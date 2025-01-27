# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Returns the (memoized) result of opt_einsum.contract_path."""
# Note: We use einsum_call=True, which is an internal api for opt_einsum,
# to get the contraction path without having opt_einsum perform the actual
# contractions.
_, contractions = opt_einsum.contract_path(
    equation,
    *shaped_inputs_tuple,
    optimize=optimize,
    einsum_call=True,
    use_blas=True)
# Return a tuple so that the cached value is not mutable.
indices_and_equations = tuple([(expr[0], expr[2]) for expr in contractions])
exit(indices_and_equations)
