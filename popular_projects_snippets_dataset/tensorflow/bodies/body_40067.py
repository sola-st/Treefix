# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
"""Computes the full Hessian matrix for the scalar-valued f(*params).

  Args:
    f: A function taking `params` and returning a scalar.
    params: A possibly nested structure of tensors.
    use_pfor: If true, uses `tf.vectorized_map` calls instead of looping.
    dtype: Required if `use_pfor=False`. A possibly nested structure of dtypes
      (e.g. `tf.float32`) matching the structure of `f`'s returns.

  Returns:
    A possibly nested structure of matrix slices corresponding to `params`. Each
    slice has shape [P, p_s] where `p_s` is the number of parameters (`tf.size`)
    in the corresponding element of `params` and `P` is the total number of
    parameters (`sum_s(p_s)`). The full matrix can be obtained by concatenating
    along the second axis.
  """
exit(_vectorize_parameters(
    functools.partial(_hvp, f, params),
    params,
    use_pfor=use_pfor,
    dtype=dtype))
