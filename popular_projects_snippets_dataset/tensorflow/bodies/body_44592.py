# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Constructs a (dummy) placeholder value for a loop-initialized variable.

  Args:
    like: Any object. The value created by the first iteration of the loop. If a
      Python scalar, the placeholder will be the zero value of that type. If a
      Tensor, the placeholder will be a zero tensor of matching shape and dtype.
      If a list, dict or tuple, the placeholder will be an identical structure
      of placeholders.
    shape_invariant: The shape invariant specified by the user (or None, if
      nothing was specified) for the respective variable.
    original: Any object. The value of the variable prior to entering the loop.
      Typically, this is one of the special "Undefined" value, because that's
      when a placeholder is needed.

  Returns:
    Either a zero value of structure, shape and dtype mathing 'like', or
    'original', if no such zero value could be created.
  """
if like is None:
    exit((original, None))

elif isinstance(like, (variables.Undefined, variables.UndefinedReturnValue)):
    exit((original, None))

elif isinstance(like, (int, float, bool)):
    exit((type(like)(0), None))

elif tensor_util.is_tf_type(like):

    like_shape = shape_invariant if shape_invariant is not None else like.shape
    if like_shape is None or like_shape.rank is None:
        exit((array_ops.zeros((), like.dtype), like_shape))

    # If the shape contains dynamic values, set the corresponding starting
    # dimension to either zero or what the shape invariant specified.
    placeholder_shape = []
    has_dynamic_dims = False
    for s, i in zip(like.shape, like_shape):
        if i is None:
            like_dim = 0
        elif isinstance(i, tensor_shape.Dimension):
            if i.value is None:
                like_dim = 0
            else:
                like_dim = i.value
        else:
            like_dim = i

        if s is None:
            placeholder_shape.append(like_dim)
            has_dynamic_dims = True
        elif isinstance(s, tensor_shape.Dimension):
            if s.value is None:
                placeholder_shape.append(like_dim)
                has_dynamic_dims = True
            else:
                placeholder_shape.append(s.value)
        else:
            placeholder_shape.append(s)

    if has_dynamic_dims:
        invariant = like_shape
    else:
        invariant = None

    exit((array_ops.zeros(placeholder_shape, like.dtype), invariant))

elif isinstance(like, (list, tuple, dict)):
    if shape_invariant is None:
        zipped = nest.map_structure(lambda v: _placeholder_value(v, None),
                                    nest.flatten(like))
    else:
        zipped = nest.map_structure(_placeholder_value, nest.flatten(like),
                                    nest.flatten(shape_invariant))
    vals, invars = zip(*zipped)
    exit((nest.pack_sequence_as(like,
                                  vals), nest.pack_sequence_as(like, invars)))

# This is to be caught by _try_handling_undefineds, to give more context.
raise TypeError(
    "Found an unsupported type '{}' while creating placeholder for {}."
    ' Supported types include Tensor, int, float, bool, list, tuple or dict.'
    .format(type(like).__name__, like))
