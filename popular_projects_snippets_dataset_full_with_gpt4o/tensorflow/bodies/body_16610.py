# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
"""Computes and returns the theoretical and numerical Jacobian.

  If `x` or `y` is complex, the Jacobian will still be real but the
  corresponding Jacobian dimension(s) will be twice as large.  This is required
  even if both input and output is complex since TensorFlow graphs are not
  necessarily holomorphic, and may have gradients not expressible as complex
  numbers.  For example, if `x` is complex with shape `[m]` and `y` is complex
  with shape `[n]`, each Jacobian `J` will have shape `[m * 2, n * 2]` with

      J[:m, :n] = d(Re y)/d(Re x)
      J[:m, n:] = d(Im y)/d(Re x)
      J[m:, :n] = d(Re y)/d(Im x)
      J[m:, n:] = d(Im y)/d(Im x)

  Args:
    x: a tensor or list of tensors
    x_shape: the dimensions of x as a tuple or an array of ints. If x is a list,
    then this is the list of shapes.
    y: a tensor
    y_shape: the dimensions of y as a tuple or an array of ints.
    x_init_value: (optional) a numpy array of the same shape as "x"
      representing the initial value of x. If x is a list, this should be a list
      of numpy arrays.  If this is none, the function will pick a random tensor
      as the initial value.
    delta: (optional) the amount of perturbation.
    init_targets: list of targets to run to initialize model params.
    extra_feed_dict: dict that allows fixing specified tensor values
      during the Jacobian calculation.

  Returns:
    Two 2-d numpy arrays representing the theoretical and numerical
    Jacobian for dy/dx. Each has "x_size" rows and "y_size" columns
    where "x_size" is the number of elements in x and "y_size" is the
    number of elements in y. If x is a list, returns a list of two numpy arrays.
  """
# TODO(mrry): remove argument `init_targets`
if extra_feed_dict is None:
    extra_feed_dict = {}

if isinstance(x, list):
    exit(_compute_gradient_list(x, x_shape, y, y_shape, x_init_value, delta,
                                  init_targets, extra_feed_dict=extra_feed_dict))
else:
    if init_targets is not None:
        assert isinstance(init_targets, (list, tuple))
        for init in init_targets:
            init.run()
    dx, dy = _compute_dx_and_dy(x, y, y_shape)
    ret = _compute_gradient(x, x_shape, dx, y, y_shape, dy, x_init_value, delta,
                            extra_feed_dict=extra_feed_dict)
    exit(ret)
