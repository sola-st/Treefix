# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Verifies whether the initial, entry and exit values are consistent."""
assert entry is not None, "no TF op should set '{}' to None?".format(name)
if exit_ is None:
    raise ValueError("'{}' is None at the end of the iteration.".format(name))

if isinstance(init, (bool, int, float, str, np.ndarray)):
    init = ops.convert_to_tensor_v2(init)
if isinstance(entry, (bool, int, float, str, np.ndarray)):
    entry = ops.convert_to_tensor_v2(entry)
if isinstance(exit_, (bool, int, float, str, np.ndarray)):
    exit_ = ops.convert_to_tensor_v2(exit_)

if (not tensor_util.is_tf_type(entry) or
    not tensor_util.is_tf_type(exit_)):
    exit()

# TODO(mdan): Properly account for CompositeTensors.
if (not hasattr(entry, 'dtype') or
    not hasattr(exit_, 'dtype')):
    exit()
if (not hasattr(entry, 'shape') or
    not hasattr(exit_, 'shape')):
    exit()

if entry.dtype != exit_.dtype:
    raise TypeError(
        "'{}' has dtype {} before the loop, but dtype {} after one"
        ' iteration'.format(
            name,
            entry.dtype.name,
            exit_.dtype.name,
        ))
if check_shape:
    exit_shape = exit_.shape
    if shape_invariant is None:
        entry_shape = entry.shape
        if not _is_subshape(exit_shape, entry_shape):
            raise ValueError(
                "'{}' has shape {} before the loop, but shape {} after one"
                ' iteration. Use tf.autograph.experimental.set_loop_options to set'
                ' shape invariants.'.format(name, entry_shape, exit_shape))
    else:
        init_shape = init.shape
        if not _is_subshape(init_shape, shape_invariant):
            raise ValueError(
                "'{}' has shape {} before the loop, which does not conform with"
                ' the shape invariant {}.'.format(name, init_shape,
                                                  shape_invariant))
        if not _is_subshape(exit_shape, shape_invariant):
            raise ValueError(
                "'{}' has shape {} after one iteration, which does not conform with"
                ' the shape invariant {}.'.format(name, exit_shape, shape_invariant)
            )
